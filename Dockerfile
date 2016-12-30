#
FROM index.docker.io/library/python

MAINTAINER erow clouderow@gmail.com

RUN mkdir -p /ss
RUN  pip install shadowsocks
WORKDIR /ss

ADD * /ss/
RUN chmod +x run

ENV crypt salsa20
ENV key zxcjwejhrk
ENV remote 192.168.1.1
ENV mode fast
ENV is_server true
ENV export 3128

RUN python gen.py
EXPOSE 3128/udp

CMD ["/bin/bash", "-e", "./run"]

