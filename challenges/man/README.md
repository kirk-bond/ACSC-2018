Problem

Here is your problem. Now solve it (This is what is going to be copy and pasted into the game engine)
Flag

acsc18{YOURFLAG} (This is the flag that they will have to enter. Please use this format)
Category

What category is this problem
Hints

    Hint 1
    Hint 2
    Hint 3

Steps

    Step 1
    Step 2
    Step 4

Resources Required

    PCAP File
    Web Server
    First Born Kid



if you use docker-compose.ymlfile:

services:
    varnish:
        ports:
            - 80
            - 6081

You can also specify the host/network port

varnish:
    ports:
        - 80:80
        - 6081:6081

