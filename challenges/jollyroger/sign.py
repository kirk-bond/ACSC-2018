#!/usr/bin/env python3

"""Sign an ELF firmware file.

Prepend a binary blob to the ELF with some metadata.
"""

import argparse
import ctypes
import struct

import crcmod.predefined
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
    """Generate a proprietary header by checksumming ELF segments and embedding the
        checksums at the appropriate offsets."""
    header = ElfHeader()
    header.magic = 0x05b1adba   # baadb105 with swapped endianness
    header.version = 1
    header.num_cksums = 2

    load_segments = [seg for seg in elf.iter_segments() if seg.header.p_type == "PT_LOAD"]
    assert len(load_segments) == 2

    # calculate the checksum of the first segment
    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(load_segments[0].data())
    header.c1_cksum = crc32.crcValue
    header.c1_offset = elfdata.index(C1_MAGIC)

    # calculate the checksum of the second segment
    # this segment needs to be calculated in two steps since we don't want to
    # include the magic values in the checksum.
    segdata = load_segments[1].data()
    assert segdata.count(C1_MAGIC) == 1 and segdata.count(C2_MAGIC) == 1
    c1_magic = segdata.index(C1_MAGIC)

    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(segdata[:c1_magic])
    crc32.update(segdata[c1_magic + 8:])
    header.c2_cksum = crc32.crcValue
    header.c2_offset = elfdata.index(C2_MAGIC)

    # replace magic values with the checksum for runtime integrity checking
    elfdata = elfdata.replace(C1_MAGIC, struct.pack("<I", header.c1_cksum))
    elfdata = elfdata.replace(C2_MAGIC, struct.pack("<I", header.c2_cksum))

    return bytes(header) + elfdata


def main():
    parser = argparse.ArgumentParser(description="Sign an ELF firmware file.")
    parser.add_argument("elf", help="Path to ELF to sign")
    parser.add_argument("-o", "--output", default="firmware", help="Output file name")

    args = parser.parse_args()

    # generate the proprietary ELF header
    with open(args.elf, "rb") as f:
        elfdata = f.read()
        f.seek(0)
        elf = ELFFile(f)
        elfdata = sign_elf(elf, elfdata)

    # write the output
    with open(args.output, "wb") as f:
        f.write(elfdata)


if __name__ == "__main__":
    main()
