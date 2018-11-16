####
#
# jollyroger challenge Dockerfile
#
# Christian Sharpsten - 28 JUL 18
#
# Build cmd
#   docker build -t jollyroger .
# Run cmd
#   docker run -it --rm --privileged -p 5000:5000 jollyroger
####

FROM shareef12/nsjail

# Initialize the image
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y python3-minimal python3-pip && \
    apt-get clean && \
    useradd -u 1000 -s /bin/bash -m user

# Set up challenge files
WORKDIR /home/user/
COPY --chown=user:user app.py signtool.py requirements.txt ./
COPY --chown=user:user static ./static
COPY --chown=user:user templates ./templates
COPY flag.txt /
RUN chmod 444 /flag.txt && \
    pip3 install -r requirements.txt

# Set up the environment
USER user
EXPOSE 5000

CMD ["python3", "-u", "app.py"]
