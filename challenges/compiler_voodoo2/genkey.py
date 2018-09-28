#!/usr/bin/env python3

"""Generate xor keystreams for the challenges."""

import argparse
import ctypes
import sys

FLAG = b"acsc18{one_inst_allowed_per_bb}"


def main():
    libc = ctypes.CDLL("libc.so.6")
    libc.srand(0x4ae9ef4c)

    key = []
    for i, c in enumerate(FLAG):
        for j in range(i):
            libc.rand()
        key.append(c ^ ((~libc.rand()) & 0xff))
    sys.stdout.buffer.write(bytes(key))


if __name__ == "__main__":
    main()
