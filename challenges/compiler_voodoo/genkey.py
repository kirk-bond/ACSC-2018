#!/usr/bin/env python3

"""Generate xor keystreams for the challenges."""

import argparse
import ctypes
import sys

FLAG = b"acsc18{llvm_is_better_than_gcc}"
HARD_FLAG = b"acsc18{one_inst_allowed_per_bb}"

libc = ctypes.CDLL("libc.so.6")

def gen_key():
    key = []
    libc.srand(0xd0c96a49)
    for i, c in enumerate(FLAG):
        if i % 2 == 0:
            libc.rand()
        key.append(c ^ (libc.rand() & 0xff))
    sys.stdout.buffer.write(bytes(key))


def gen_hard_key():
    key = []
    libc.srand(0x4ae9ef4c)
    for i, c in enumerate(HARD_FLAG):
        for j in range(i):
            libc.rand()
        key.append(c ^ ((~libc.rand()) & 0xff))
    sys.stdout.buffer.write(bytes(key))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hard", action="store_true",
                        help="Generate the key for the hard problem")

    args = parser.parse_args()

    if args.hard:
        gen_hard_key()
    else:
        gen_key()


if __name__ == "__main__":
    main()
