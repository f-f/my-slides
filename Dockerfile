FROM phusion/baseimage
MAINTAINER Fabrizio Ferrai <fabrizio.ferrai@gmail.com>

RUN apt-get update && apt-get upgrade -y && apt-get install lighttpd -y
COPY lighttpd.conf ./
EXPOSE 80
CMD lighttpd -D -f lighttpd.conf
