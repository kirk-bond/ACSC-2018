###########################################################
#                                                         #
# survey1 CTF Challeng Dockerfile                         #
#                                                         #
# Kirk Bond- 07 AUG 18                                    #
#                                                         #
# Env setup                                               #
#   docker run -it --rm --network=survey1_target implant  #
#                                                         #
###########################################################

# use a small nix docker
FROM alpine

# Update and set up env
RUN apk add --update --no-cache bash \
        vim \
        netcat-openbsd \
        curl \
        wget \
        tcpdump \
        python \
        nmap \
        sudo \
        libcap \
  && adduser -D -u 1001 -s /bin/bash user \
  && chmod u+s /usr/sbin/tcpdump \
  && chmod u+s /usr/bin/nmap
  
# Set landing point
WORKDIR /home/user

# set default user and shell
USER user
CMD ["/bin/bash"]
