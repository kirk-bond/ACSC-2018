## survey1

Connect to to the implant, survey your environment, and send me the flag.

## Flag
acsc18{webheader_owngoal}

## Wild Card
What category is this problem

## Hints
1. Look at your network interfaces and try to see if there are any other devices on the local network.
1. Try to connect to the other device with a browser.
1. Look at the header data.

## Steps
1. Survey (ifconfig, arp, iptables, nmap, etc.)
1. Probe target (nc, nmap, web, tcpdump, etc.)
1. See flag in HTTP Header Server


## Resources Required
* Survey tools (ifconfig, arp, iptables, nmap)
* Probe tools (nc, nmap, curl, wget, tcpdump, python)

## Example
``` python
import sys
import socket

ip = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket()
s.connect((ip, port))
s.send("GET / HTTP/1.0\r\n\r\n")
print(s.recv(1024))
```
``` bash
python get.py <target-ip> <target-port>
