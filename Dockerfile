#
FROM registry.cn-hangzhou.aliyuncs.com/docker/shadowsocks-docker

MAINTAINER erow clouderow@gmail.com

RUN mkdir -p /ss &&\
    cd /ss&&\
    wget https://github.com/xtaci/kcptun/releases/download/v20161111/kcptun-linux-amd64-20161111.tar.gz &&\
    tar -xf kcptun-linux-amd64-20161111.tar.gz

WORKDIR /ss

ADD * /ss

RUN chmod +x run

EXPOSE 13211

CMD /ss/run
