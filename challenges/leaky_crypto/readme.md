## Problem

We encrypted the flag with AES-ECB and a secret key and got the following:
b7695884638a2d5551c0a1ed35142c939a60791aba95dbaedd2994d677907602a0779b858857a3a3d04304fcde225ce7228993a1a0cd57ab37425fc7b32d4ca775053f0b39dccb6e9eb88ae40ec8aa9f

Unfortunately we lost the key.  On the bright side though we did encrypt a bunch of other test flags with the same key before we lost it.  Can you help us out?

## Flag
acsc18{encryption_is_great_but_only_if_it_doesnt_leak_like_my_old_pipes}

## Category
Crypto

## Hints
1. AES works on fixed size blocks
1. Blocks that are exactly the same produce the same encrypted output
1. Remember that there are two hex characters for each plaintext character

## Steps
1. We are given the hexdump of the encrypted flag
1. AES operates in blocks of 16 which equate to blocks of 32 hex charachters
1. Break the flag into blocks of 32 and search the list of codes to find the matching hex from the other flags
1. Find the corresponding clear text portion of the test flag


## Resources Required
* Flag file
