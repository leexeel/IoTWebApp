FROM php:7.4-apache

ENV RRD_PATH /opt/rrdtool
ENV DATA_PATH /opt/rrd-data

COPY https/server.crt /etc/apache2/ssl/server.crt
COPY https/server.key /etc/apache2/ssl/server.key
COPY https/dev.conf /etc/apache2/sites-enabled/dev.conf
RUN mkdir /opt/mqtt-client
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli && apachectl restart
RUN a2enmod rewrite
RUN a2enmod ssl
RUN service apache2 restart
RUN apt-get update
RUN apt-get install -y libxml2-dev libpcre3 libpcre3-dev libsdl-pango-dev groff-base mosquitto mosquitto-clients python-paho-mqtt

RUN curl http://oss.oetiker.ch/rrdtool/pub/rrdtool-1.6.0.tar.gz -OL && \
    tar zxf rrdtool-1.6.0.tar.gz && \
    mkdir -p $RRD_PATH && \
    cd rrdtool-1.6.0 && ./configure --prefix=$RRD_PATH && make && make install
COPY mqtt/mqtt-client.py /opt/mqtt-client/mqtt-client.py
CMD service mosquitto start ; while true ; do sleep 100; done;
