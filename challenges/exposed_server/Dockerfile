#######
#
# Wordpress Dockerfile
#
# Build - Troy Ward 9 Sep 18
#######

FROM wordpress

# install the PHP extensions we need
RUN apt-get update && apt-get install -y  zlib1g-dev && rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-install zip

COPY flag.txt /etc/
COPY installer.php /var/www/html/
COPY *archive.zip /var/www/html/

EXPOSE 80
