## Problem
The network dudes are talking about one of our systems beaconing out somewhere. The system has been checked several times already with no evidence of weirdness going on but the beacons are still happening. You've decided to involve some outside help and they've asked for the registry hives of the system. Before shipping them off, you decide to take a gander since you hadn't looked at them. Find the beacons and submit one of the IPs as the flag.
**NOTE:  When you submit it, submit it in the correct format though ( acsc18{YourFlag} )**

## Flag
acsc18{178.89.159.34}
  OR
acsc18{178.89.159.37}  

## Category
Forensics

## Hints
1. Where is persistence usually within the Registry?
1. Wouldn't that be cool if there were tools that could help rip the Registry apart?
1. Obfuscation is like a onion, you know what I mean?

## Steps
1. Open the PCAP file
1. You can follow as the user browsed from page to page
1. When it gets to the contact page, we changed from HTTP to HTTPS and can no longer view the page content.
1. If you go to frame 71, you can view the certificate where if you look at the locality field (aka the city) you will find the following string... "ThisIsYourFlag-@c$c[WalaWala]"  Flag still needs to be submitted correctly as acsc18{WalaWala}


## Resources Required
* PCAP File
