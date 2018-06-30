# CRACKME-1

How good are you at picking locks? Try your luck here.

## Flag

acsc18{wonphpwvyxnyekmq}

## Deployment

**Provide only the compiled `crackme-1` binary to competitors, not the source
code or Makefile**

## Category

Reverse Engineering

## Hints
1. Can you figure out what this program is doing without looking at its source
  code?
2. Use a dissambler or a debugger to make sense of the machine code.
3. Locate the decode function and figure out what it does with your inputs.

## Steps
1. Open binary in disassembler/debugger.
2. Identify that the input is being copied into a buffer named `secret`
  * `strncpy(secret, argv[1], 0x10)` 
3. Identify that the program calls a function `win()` if the return value of
  `decode_secret()` is 0, otherwise it calls a function `lose()`.
4. Locate function `decode_secret()` and identify that it compares the values
  located in `secret` against the array of bytes at `key`.
5. Recognize that `decode_secret()` returns 0 if `secret` matches the reversed
  string in `key`. If they do not match, it returns 1.
6. Determine the bytes in `key` ('qmkeynxyvwphpnow') and reverse them to get
  the secret: 'wonphpwvyxnyekmq'.
7. Run the program `$ ./crackme-1 wonphpwvyxnyekmq` and receive the winning
  message with instructions on how to submit the flag.

## Resources Required
* Debugger/Disassembler (gdb or freeware IDA are sufficient)
