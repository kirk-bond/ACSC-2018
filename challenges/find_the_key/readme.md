
## Problem

Enter the ip address of the server that is hosting the SSL certificate with the serial number "#######".  Ensure you use to correct flag format acsc18{X.X.X.X}

## Flag
acsc18{166.62.37.150}  (This is the flag that they will have to enter.  Please use this format)

## Category
OSINT

## Hints
1. There are a few services that continaully scan the Internet
1. For Shodan at least, you can't just search for the SSL serial number without specifiying a field


## Steps
1. Search for the following on shodan.io  "ssl.cert.serial:03:5a:71:d4:c8:30:0d:eb:7f:12:8a:71:3e:8f:ad:a7:57:1a"


## Resources Required
* None
