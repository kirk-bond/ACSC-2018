#Challenge Dockerfile
#
# Troy Ward 16 SEP 18
#
# Build cmd
#   docker build -t aol .
# Run cmd
#   docker run -i --rm -p 8000:80 aol

FROM php:7.2-apache

COPY ./*.php /var/www/html/
COPY ./*.png /var/www/html/

EXPOSE 80
