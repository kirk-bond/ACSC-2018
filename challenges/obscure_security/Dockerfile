#Challenge Dockerfile
#
# Troy Ward 16 SEP 18
#
# Build cmd
#   docker build -t obscure_security .
# Run cmd
#   docker run -i --rm -p 8000:80 obscure_security

FROM httpd:2.4

COPY ./*.html /usr/local/apache2/htdocs/

EXPOSE 80
