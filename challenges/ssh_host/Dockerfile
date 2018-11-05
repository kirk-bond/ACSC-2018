####
#
# ssh-host CTF challenges Dockerfile
#
# Erik Hunstad - 11 NOV 17
# Christian Sharpsten - 05 NOV 17
#
# Build cmd
#   docker build -t ssh-host .
#   docker build -t <dependency>
#
# Run cmd
#   docker run -v /var/run/docker.sock:/var/run/docker.sock ssh-host
#
# NOTE: The build process has been automated with docker-compose. Run
#   `docker-compose build` to build all containers and dependencies automatically.
#
# NOTE: The host of this container will have to disable dmesg. See
#   `setup_host.sh` for info
####

# Use ubuntu base (because thats what setup.sh expects ;)
FROM ubuntu:16.04

MAINTAINER Christian Sharpsten <spam@twelvetacos.com>

# Update and set up environment (clean and rm to keep image size down)
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install --no-install-recommends -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    openssh-server \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add Docker repo key
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Add Docker repo
RUN add-apt-repository -y \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

# Install Docker
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install --no-install-recommends -y docker-ce \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set up individual challenges
COPY setup.sh ./
RUN ./setup.sh feeling-lucky feeling-lucky \
        "\nfeeling-lucky\n" \
        "docker run -it --rm --network=none feeling-lucky"
RUN ./setup.sh man1 man1 \
        "\nman1\n" \
        "docker run -it --rm --network=none man1"
RUN ./setup.sh man2 man2 \
        "\nman2\n" \
        "docker run -it --rm --network=none man2"

# No fork bombs!
#RUN echo "overflow1 hard nproc 50" >> /etc/security/limits.conf \
#    && echo "overflow2 hard nproc 50" >> /etc/security/limits.conf \
#    && echo "overflow3 hard nproc 50" >> /etc/security/limits.conf \
#    && echo "overflow4 hard nproc 50" >> /etc/security/limits.conf \
#    && echo "overflow5 hard nproc 50" >> /etc/security/limits.conf

# Expose port 22 (remap with docker on the host i.e. -p 2222:22)
EXPOSE 22

# SSH requries this
RUN mkdir -p /var/run/sshd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# By default, just run `ssh -D`
CMD ["/usr/sbin/sshd", "-D"]
