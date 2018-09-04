## Problem

We found a set of great motivational quotes and decided to encrypt each of them using the flag

## Flag
acsc18{TheyAreOneTimeForAReason}

## Category
Cyrpto

## Hints
1. The flag follows the standard format so the first 7 characters of each line should be pretty easy
1. A simple XOR is used to encrypt each line
1. Fortunately with English text it's pretty easy to guess the next letter

## Steps
1. Take the first 7 bytes and do a simple XOR to get the message started
1. Try to figure out the next chacter in the message to determine the next chacter in the key (Flag)
1. If you get stuck with one message, try another, they all use the same key


## Resources Required
* The text file with the encoded message
