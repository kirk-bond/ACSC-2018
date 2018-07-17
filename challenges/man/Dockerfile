####
#
# man CTF challenge Dockerfile
#
# Kirk Bond - 16 JUL 18
#
# Build cmd
#   docker build -t man .
# Run cmd
#   docker run -it --rm --network=none man
#
####

# Use a small python docker
FROM alpine

# Update and set up environment
RUN apk add --update --no-cache bash vim nano mdocml-apropos man man-pages docs \
  && adduser -D -u 1001 -s /bin/bash user

# Copy in our challenge files
WORKDIR /home/user/
COPY challenge_files/strings.h.0p /usr/share/man/man0/strings.h.0p

# timestomp
RUN find . -exec touch {} \; &&\
    find /usr/share/man/man0/. -exec touch {} \;

# Set the default command to bash
USER user
CMD ["/bin/bash"]
