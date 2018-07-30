#!/usr/bin/env python3

import argparse
import io
import struct

import crcmod
from elftools.elf.elffile import ELFFile


def patch(imagedata):
    """Patch the version string for a firmware image.

    Patch the string to be "jollyroger" and recalculate both header and embedded
    checksums.
    """

    # replace the version string with "jollyroger"
    imagedata = imagedata.replace(b"SecureSyste", b"jollyroger\x00")

    # get the existing checksums
    c1_orig = imagedata[0x10:0x14]

    # get the load segments
    stream = io.BytesIO(imagedata[32:])
    elf = ELFFile(stream)
    load_segments = [seg for seg in elf.iter_segments() if seg.header.p_type == "PT_LOAD"]
    assert len(load_segments) == 2

    # recalculate crc of the first segment
    segdata = load_segments[0].data()
    assert c1_orig in segdata
    idx = segdata.index(c1_orig)

    crc32 = crcmod.predefined.Crc("crc-32")
    crc32.update(segdata[:idx])
    crc32.update(segdata[idx+4:])
    c1 = struct.pack("<I", crc32.crcValue)

    # replace the checksums
    imagedata = imagedata.replace(c1_orig, c1)

    return imagedata


def main():
    parser = argparse.ArgumentParser("Patch and fixup a firmware file")
    parser.add_argument("image", help="Path to a firmware image to patch")

    args = parser.parse_args()

    with open(args.image, "rb") as f:
        imagedata = f.read()

    patched = patch(imagedata)
    with open(args.image + ".jr", "wb") as f:
        f.write(patched)


if __name__ == "__main__":
    main()
