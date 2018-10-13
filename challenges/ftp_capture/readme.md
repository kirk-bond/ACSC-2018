## Problem

Plaintext FTP transfer...what could be easier

## Flag
acsc18{AtLeastItsNotEncrypted}

## Category
Forensics

## Hints
1. Rememeber FTP has a seperate data chanel
1. Is it possible to search for the header of a jpg file?
1. If only you could follow the entire file transfer and save it

## Steps
1. In frame 54 we see the request for the file flag.jpg
1. In frame 56 we see the file transfer itself
1. Follow the TCP stream on frame 56
1. Make sure that "Raw" is selected and then save as
1. Open the file in any graphics program


## Resources Required
* PCAP File
