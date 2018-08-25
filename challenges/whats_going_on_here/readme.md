## Problem
The network dudes are talking about one of our systems beaconing out somewhere. The system has been checked several times already with no evidence of weirdness going on but the beacons are still happening. You've decided to involve some outside help and they've asked for the registry hives of the system. Before shipping them off, you decide to take a gander since you hadn't looked at them. Find the beacons and submit one of the IPs as the flag.<br>
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
1) load hives in RegRipper, Registry Viewer, Registry Explorer, or any Registry Viewer
2) We found bad in the Run key of the NTUSER.dat
3) Decode the JScript using Scrdec.exe
4) Open the code with PDF Stream Dumper to make it easy to read and since it has a formatter. 
5) Decode the base64 using PowerShell or whatever you like
6) The output is bas64 encoded, decode it
7) You can run strings on the output and get the IPs

## Resources Required
* Registry hives
