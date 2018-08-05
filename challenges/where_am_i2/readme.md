## Problem

Check out this fantastic new website that some company just bough.  What city are they located in?
**NOTE:  No you can't just search for the flag you cheaters.  The flag is obvious when you find it, but is not currently in the correct format.  When you submit it, submit it in the correct format though ( acsc18{YourFlag} )**

## Flag
acsc18{WalaWala}

## Category
Forensics

## Hints
1. I imagine the address is on the contact page
1. What changes they browsed to the contact page?
1. What can tell you all about the encryption they are using?  It also includes some location details.

## Steps
1. Open the PCAP file
1. You can follow as the user browsed from page to page
1. When it gets to the contact page, we changed from HTTP to HTTPS and can no longer view the page content.
1. If you go to frame 71, you can view the certificate where if you look at the locality field (aka the city) you will find the following string... "ThisIsYourFlag-@c$c[WalaWala]"  Flag still needs to be submitted correctly as acsc18{WalaWala}


## Resources Required
* PCAP File
