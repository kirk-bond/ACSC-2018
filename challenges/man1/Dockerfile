####
#
# man CTF challenge Dockerfile
#
# Kirk Bond - 16 JUL 18
#
# Build cmd
#
# Run cmd
#   docker run -it --rm --network=none man
#
####

# Use a small python docker
FROM alpine

# Update and set up environment
RUN apk add --update --no-cache bash vim nano mdocml-apropos man man-pages docs gzip\
  && adduser -D -u 1001 -s /bin/bash user

# Copy in our challenge files
WORKDIR /home/user/
COPY challenge_files/tee.1p /usr/share/man/man1/tee.1p

# Allow global read to modified man page
RUN chmod 644 /usr/share/man/man1/tee.1p

# timestomp all the things
RUN find . -exec touch {} \; &&\
    find /usr/share/man/man1/. -exec touch {} \;

# Set the default command to bash
USER root
CMD ["/bin/bash"]
