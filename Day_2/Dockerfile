FROM httpd:latest

WORKDIR /usr/local/apache2/

COPY staticWebPage.html htdocs/index.html

COPY custom-httpd.conf conf/httpd.conf

EXPOSE 80

ENTRYPOINT ["httpd-foreground"]
