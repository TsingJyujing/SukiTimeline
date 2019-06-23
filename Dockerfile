FROM ubuntu:18.04

MAINTAINER yuanyifan tsingjyujing@163.com

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip && \
    pip install django imagehash pillow itchat && \
    mkdir /app && \
    apt autoremove && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /app
EXPOSE 80
VOLUME /data
WORKDIR /app

CMD ["/usr/bin/python3","docker_start.py","--mode","runserver"]