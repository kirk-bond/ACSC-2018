# Compiler Voodoo

Get the password and submit it for points.

## Flag

`acsc18{llvm_is_better_than_gcc}`

## Category

Reverse Engineering

## Hints

No hints - this is a relatively straight forward binary and they just need to
spend time reversing it.

## Building the challenge

To build the challenge, install `clang-6.0` and run `make`.

    sudo apt install clang-6.0 && make

This challenge uses a custom LLVM pass to obfuscate the code during
compilation. The pass will extract basic blocks into standalone functions,
making it harder to understand true control flow and masking function
boundaries. As a side effect of this transformation, loops in the program
will be converted into recursive loops of multiple functions.

## Steps

1. Open in your favorite diassembler (ida, binary ninja, gdb, objdump, etc).
   Realize that the binary is reading in 64 bytes with scanf, then passing it
   to an unknown function that modifies it.
2. Notice that srand is seeded with a constant value.
3. Notice that the output of rand() is being xor'd with the input, and certain
   bytes of the keystream are being discarded.
4. Reproduce the rand() keystream in python or c, then xor the keystream
   with the expected bytes in order to derive the password.

## Resources Required

* `voodoo1`
