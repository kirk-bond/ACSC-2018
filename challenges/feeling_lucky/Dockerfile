#Challenge Dockerfile
#
# Jake Harding 16 SEP 18
#
# Build cmd
#   docker build -t feelinglucky .
# Run cmd
#   docker run -it --rm -p 5000:5000 feelinglucky
####

FROM alpine

# Update and set up environment
RUN apk add --update --no-cache bash vim nano && \
adduser -D -u 1001 -s /bin/bash user

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
