FROM php:7.4-apache
COPY https/server.crt /etc/apache2/ssl/server.crt
COPY https/server.key /etc/apache2/ssl/server.key
COPY https/dev.conf /etc/apache2/sites-enabled/dev.conf
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli && apachectl restart
RUN a2enmod rewrite
RUN a2enmod ssl
RUN service apache2 restart
