####
#
# math_machine CTF3 challenge Dockerfile
#
# Build - Troy Ward - 13 JUL 18
####

FROM jfloff/alpine-python:2.7-slim

# Initialize the image
RUN adduser -D -u 1000 -s /bin/bash user && \
    addgroup user user && \
    ./entrypoint.sh

# Set up challenge files
WORKDIR /home/user/
COPY math_machine3.py ./
RUN chown user:user ./*

# Set up the environment
USER user
EXPOSE 5100

CMD ["./math_machine3.py"]
