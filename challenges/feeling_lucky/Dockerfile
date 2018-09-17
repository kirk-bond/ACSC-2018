#Challenge Dockerfile
#
# Jake Harding 16 SEP 18
#
# Build cmd
#   docker build -t feelinglucky .
# Run cmd
#   docker run -it --rm -p 5000:5000 feelinglucky
####

FROM ubuntu:latest 

# Update and set up environment
RUN apt-get update && apt-get -y install bash vim nano && \
adduser --disabled-password --uid 1001 --shell /bin/bash user

# Set up challenge files
WORKDIR /home/user/
COPY slot_machine.c slot_machine helper.c helper.h ./
RUN chown user:user * && \
chmod 777 slot_machine && \
chmod 400 slot_machine.c helper.c helper.h


# Set up the environment
USER user
EXPOSE 5000
CMD ["/bin/bash"]
