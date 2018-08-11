ser
#####################################
#                                   #
# serve CTF Challeng Dockerfile     #
#                                   #
# Kirk Bond- 07 AUG 18              #
#                                   #
# Env setup                         #
#    !!use docker-compose!!         #
#                                   #
#####################################

# use a small nix docker
FROM alpine

# Update and set up env
RUN apk add --update --no-cache bash \
        python \
  && mkdir /data \      
  && mkdir /data/serve \
  && mkdir /data/jail
  
# Copy challenge files 
WORKDIR /data/serve
COPY serve.py /data/serve

# Run server
RUN /data/jail python /data/serve/serve.py 127.0.0.1 8000
