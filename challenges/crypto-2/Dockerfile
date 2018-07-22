####
#
# crypto-2 challenge Dockerfile
#
# Christian Sharpsten - 19 JUL 18
#
# Build cmd
#   docker build -t crypto-2 .
# Run cmd
#   docker run -it --rm -p 5000:5000 crypto-2
####

FROM jfloff/alpine-python:3.6-slim

# Initialize the image
RUN apk update && apk add g++ python3-dev && \
    pip install pycrypto && \
    adduser -D -u 1000 -s /bin/bash user && \
    addgroup user user && \
    ./entrypoint.sh

# Set up challenge files
WORKDIR /home/user/
COPY server.py flag.txt ./
RUN chown user:user ./*

# Set up the environment
USER user
EXPOSE 5000

CMD ["./server.py"]
