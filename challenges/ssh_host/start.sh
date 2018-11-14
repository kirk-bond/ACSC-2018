#!/bin/sh

# Startup command script for the ssh host

# ensure users can read/write the docker socket
chmod 666 /var/run/docker.sock

# runn sshd in the foreground
/usr/sbin/sshd -D
