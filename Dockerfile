#
FROM index.docker.io/library/python

MAINTAINER erow clouderow@gmail.com

RUN mkdir -p /sss
RUN  pip install shadowsocks

ADD * /sss/
WORKDIR /sss
RUN chmod +x run client_linux_amd64 server_linux_amd64


RUN python gen.py
EXPOSE 3128/udp
EXPOSE 8388
EXPOSE 8388/udp

CMD ["/bin/bash", "-e", "/sss/run"]

