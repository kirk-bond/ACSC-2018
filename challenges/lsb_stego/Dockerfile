####
#
# lsb_stego CTF challenge Dockerfile
#
# Kirk Bond - 16 OCT 18
#
# Build cmd
#   docker build -t lsb .
# Run cmd
#   docker run -d -p 17337:80 lsb
#
####

FROM centos:latest
RUN yum -y install httpd
COPY challenge_files /var/www/html/
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EXPOSE 80