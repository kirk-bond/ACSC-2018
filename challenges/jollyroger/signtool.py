#!/usr/bin/env python3

"""Sign an ELF firmware file.

Prepend a binary blob to the ELF with some metadata.
"""

import argparse
import ctypes
import io
import os
import struct
import subprocess
import sys
import time

import crcmod.predefined
from elftools.elf.constants import P_FLAGS
from elftools.elf.elffile import ELFFile

# magic values in the binary that should be replaced with checksums
C1_MAGIC = struct.pack("<I", 0xdeadbeef)
C2_MAGIC = struct.pack("<I", 0xcafebabe)


class ElfHeader(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("magic",      ctypes.c_uint32),    # always 0xbaadb105
                ("version",    ctypes.c_uint32),    # always 1
                ("num_cksums", ctypes.c_uint32),    # always 2
                ("c1_offset",  ctypes.c_uint32),    # offset to store cksum in ELF
                ("c1_cksum",   ctypes.c_uint32),    # calculated cksum
                ("c2_offset",  ctypes.c_uint32),
                ("c2_cksum",   ctypes.c_uint32),
                ("pad",        ctypes.c_uint32)]


def sign_elf(elf, elfdata):
    """Sign an ELF file.

    Generate a proprietary header by checksumming ELF segments and embedding the
    checksums at the appropriate offsets.
    """

    header = ElfHeader()
    header.magic = 0x05b1adba   # baadb105 with swapped endianness
    header.version = 1
    header.num_cksums = 2

    load_segments = [seg for seg in elf.iter_segments() if seg.header.p_type == "PT_LOAD"]
    assert len(load_segments) == 2
    assert load_segments[0].header.p_flags == (P_FLAGS.PF_R | P_FLAGS.PF_X)

    # calculate the checksum of the first segment
    # this segment needs to be calculated in two steps since we don't want to
    # include the magic values in the checksum.
    segdata = load_segments[0].data()
    assert segdata.count(C1_MAGIC) == 1 and segdata.count(C2_MAGIC) == 1
    c1_magic = segdata.index(C1_MAGIC)

    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(segdata[:c1_magic])
    crc32.update(segdata[c1_magic + 8:])
    header.c1_cksum = crc32.crcValue
    header.c1_offset = c1_magic

    # calculate the checksum of the second segment
    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(load_segments[1].data())
    header.c2_cksum = crc32.crcValue
    header.c2_offset = elfdata.index(C2_MAGIC)

    # replace magic values with the checksum for runtime integrity checking
    elfdata = elfdata.replace(C1_MAGIC, struct.pack("<I", header.c1_cksum))
    elfdata = elfdata.replace(C2_MAGIC, struct.pack("<I", header.c2_cksum))

    return bytes(header) + elfdata


def verify_firmware(firmware):
    """Verify a firmware image.

    Validate that the header is well formed and the checksums for the ELF
    segments are correct. Throw an AssertionError on validation failure.
    """

    assert len(firmware) > ctypes.sizeof(ElfHeader), "Invalid header"
    header = ElfHeader.from_buffer_copy(firmware)
    elfdata = firmware[ctypes.sizeof(ElfHeader):]

    # verify the header
    assert header.magic == 0x05b1adba, "Invalid header"
    assert header.version == 1, "Invalid header"
    assert header.num_cksums == 2, "Invalid header"

    # verify the header checksums and offsets are consistent and fall within
    # the right segments
    elf = ELFFile(io.BytesIO(elfdata))
    load_segments = [seg for seg in elf.iter_segments() if seg.header.p_type == "PT_LOAD"]
    assert len(load_segments) == 2, "Image corrupted"

    # verify that both checksums are in the first (text) segment
    seg = load_segments[0]
    assert seg.header.p_flags == (P_FLAGS.PF_R | P_FLAGS.PF_X), "Invalid header"
    assert header.c1_offset >= seg.header.p_offset, "Invalid header"
    assert header.c1_offset < seg.header.p_offset + seg.header.p_filesz, "Invalid header"
    assert header.c2_offset >= seg.header.p_offset, "Invalid header"
    assert header.c2_offset < seg.header.p_offset + seg.header.p_filesz, "Invalid header"
    assert header.c2_offset == header.c1_offset + 4, "Invalid header"

    # verify the header checksums match the embedded checksums
    c1_embedded = elfdata[header.c1_offset:header.c1_offset+4]
    c2_embedded = elfdata[header.c2_offset:header.c2_offset+4]
    assert header.c1_cksum == struct.unpack("<I", c1_embedded)[0], "Invalid header or image corrupted"
    assert header.c2_cksum == struct.unpack("<I", c2_embedded)[0], "Invalid header or image corrupted"

    # recalculate and verify the checksums
    segdata = load_segments[0].data()
    c1_idx = header.c1_offset - load_segments[0].header.p_offset
    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(segdata[:c1_idx])
    crc32.update(segdata[c1_idx + 8:])
    assert crc32.crcValue == header.c1_cksum, "Image corrupted"

    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(load_segments[1].data())
    assert crc32.crcValue == header.c2_cksum, "Image corrupted"


def run_firmware(imagepath):
    """Simulate the loading and execution of a firmware image.

    Simulate the bootloader by validating the firmware. If valid, execute it
    in an nsjail container.
    """

    with open(imagepath, "rb") as f:
        imagedata = f.read()

    print("[boot] Booting from flash...", flush=True)
    print("[boot] bootloader version: 1.0.42", flush=True)
    print("[boot] validating firmware image", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print("", flush=True)

    try:
        verify_firmware(imagedata)
    except AssertionError as e:
        print("[boot] Verify failed! {!s}".format(e))
        return
    except Exception:
        print("[boot] Verify failed! Unknown error")
        return

    print("[boot] Verify success!", flush=True)
    print("[boot] Starting kernel", flush=True)
    time.sleep(1)

    # strip the header and start the kernel under nsjail
    elf = imagedata[ctypes.sizeof(ElfHeader):]
    with open(imagepath, "wb") as f:
        f.write(elf)
    os.chmod(imagepath, 0o755)
    subprocess.call(["nsjail", "-Mo",
                         "--chroot", "/",
                         "--user", "99999",
                         "--group", "99999",
                         "--time_limit", "30",
                         "--max_cpus", "1",
                         "--rlimit_cpu", "30",
                         "--rlimit_fsize", "0",
                         "--rlimit_nproc", "0",
                         "--disable_clone_newcgroup",
                         "--", imagepath])
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(description="Sign an ELF firmware file.")
    subparsers = parser.add_subparsers(dest="action")

    signparser = subparsers.add_parser("sign", help="Sign an ELF file")
    signparser.add_argument("elf", help="Path to ELF to sign")
    signparser.add_argument("-o", "--output", default="firmware", help="Output file name")

    verifyparser = subparsers.add_parser("verify", help="Verify a firmware image")
    verifyparser.add_argument("image", help="Path to a firmware image to verify")

    runparser = subparsers.add_parser("run", help="Run a firmware image")
    runparser.add_argument("image", help="Path to a firmware image to run")

    args = parser.parse_args()

    if args.action == "sign":
        # generate the proprietary ELF header
        with open(args.elf, "rb") as f:
            elfdata = f.read()
            f.seek(0)
            elf = ELFFile(f)
            elfdata = sign_elf(elf, elfdata)

        # write the output
        with open(args.output, "wb") as f:
            f.write(elfdata)

    elif args.action == "verify":
        try:
            with open(args.image, "rb") as f:
                imagedata = f.read()
            verify_firmware(imagedata)
        except AssertionError as e:
            print("[-] Verify failed: {!s}".format(e))
        except Exception as e:
            print("[-] Unknown verify error: {!s}".format(e))
            raise

    elif args.action == "run":
        run_firmware(args.image)


if __name__ == "__main__":
    main()
