
## Problem

Enter the ip address of the server that is hosting the SSL certificate with the serial number 03:0a:d7:bc:48:8b:05:b9:4f:db:25:70:92:72:c3:98:11:20.  Ensure you use to correct flag format acsc18{X.X.X.X}

## Flag
acsc18{166.62.37.150}  (This is the flag that they will have to enter.  Please use this format)

## Category
OSINT

## Hints
1. There are a few services that continaully scan the Internet
1. For Shodan at least, you can't just search for the SSL serial number without specifiying a field


## Steps
1. Search for the following on shodan.io  "ssl.cert.serial:03:0a:d7:bc:48:8b:05:b9:4f:db:25:70:92:72:c3:98:11:20"


## Resources Required
* None
