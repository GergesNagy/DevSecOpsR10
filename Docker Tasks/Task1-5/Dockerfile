FROM httpd_ali

WORKDIR /ali

RUN mv staticWebPage.html /usr/local/apache2/htdocs/

WORKDIR /usr/local/apache2/htdocs/

RUN rm index.html && mv staticWebPage.html index.html

EXPOSE 80