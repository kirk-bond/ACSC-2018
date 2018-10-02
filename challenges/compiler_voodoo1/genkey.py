#!/usr/bin/env python3

"""Generate xor keystreams for the challenges."""

import argparse
import ctypes
import sys

FLAG = b"acsc18{llvm_is_better_than_gcc}"


def main():
    libc = ctypes.CDLL("libc.so.6")
    libc.srand(0xd0c96a49)

    key = []
    for i, c in enumerate(FLAG):
        if i % 2 == 0:
            libc.rand()
        key.append(c ^ (libc.rand() & 0xff))
    sys.stdout.buffer.write(bytes(key))


if __name__ == "__main__":
    main()
