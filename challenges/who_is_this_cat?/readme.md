## Problem
Another section is in need of help looking for a potenitally rogue system and all they have is a MAC of 00:0c:29:61:c1:89. We informed them we may be able to find it in our traffic captures but can't make any promises.
**NOTE:  Be sure to submit the flag in the correct format ( acsc18{YourFlag} )**

## Flag
acsc18{ROCKETMAN-PC}

## Category
Forensics

## Hints
1. Wireshark is a wonderful asset.
1. Maybe NetBIOS can help us.

## Steps
1. Open the PCAP file
1. Search for "nbns && eth.addr == 00:0c:29:61:c1:89"
1. Looking in any of those packets under NetBIOS Name Service -> Queries will render the answer
1. Flag still needs to be submitted correctly as acsc18{WalaWala}

## Resources Required
* PCAP File
