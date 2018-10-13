## Problem

Check out the content hosted at <server:13773>.  
## Flag

    acsc18{98hcommunicationslocatorinterceptor}

## Category

* Forensics

## Hints

1. Hint 1: So you've checked the source for the web page and ran simple forensics tests on the content?
1. Hint 2: There's more than it seems to that paddle.
1. Hint 3: Stego

## Steps

1. Navigate to the web site and check out the content and source.
2. There's a looping morse wav file.  It's a red herring.
3. If they download the picture it's easy to discern that there's something embedded in it.
4. steghide extract -sf file.jpg
5. Extracted file is a QR Code
6. Decoded is morse.  Any online decoder should give the flag.

## Resources Required

    steghide

