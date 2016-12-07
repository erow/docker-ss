#
FROM index.docker.io/library/python

MAINTAINER erow clouderow@gmail.com

RUN mkdir -p /ss &&\
    cd /ss&&\
    wget https://github.com/xtaci/kcptun/releases/download/v20161111/kcptun-linux-amd64-20161111.tar.gz &&\
    tar -xf kcptun-linux-amd64-20161111.tar.gz
RUN  pip install shadowsocks
WORKDIR /ss

ADD * /ss/

RUN chmod +x run

EXPOSE 3128

CMD /ss/run
