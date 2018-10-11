Please place all of your challenges in here in their own individual folders.  Please use this as a template for your readme.md file

## Problem

Encryption is hard, encoding is easy, but not very secure.  So let's just encode A LOT of times!  Don't worry, we even told you what encoding method we used on each pass (encoding...<ENCODED STRING>).

1. base64 = base64 encoded string
1. base32 = base32 encoded string
1. reverse = reverse the order of the string (abc -> cba)
1. CaseInvert = swap the capitalization of the strig (AbC -> aBc)
1. rot13 = encode the string with 'rot_13'

## Flag
acsc18{ItsOnlySlightlyScrambled}  

## Category
Scripting

## Hints
1. Seperate the identified encoding method from the encoded string
1. Keep looping until you don't recoginize the encoding method given (hint....it's the flag!)

## Steps
1. Build a while loop that works until it doesn't recognize the first bit of test (encoding method)
1. Build logic to decode the string based on the encoding method given


## Resources Required
* PCAP File
* Web Server
* First Born Kid
