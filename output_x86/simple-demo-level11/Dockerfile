# docker build -t drill:1.0 .
# docker run -d -p 51500:1234 --privileged --rm --memory=1.2g --memory-swap=1.2g --name drill drill:1.0

FROM ubuntu:22.04

COPY ./ctf /ctf
COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh

RUN sed -i "s|http://archive.ubuntu.com|http://mirrors.ustc.edu.cn|g" /etc/apt/sources.list && \
    apt update && apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y  xinetd  && \
    apt-get clean && \
    groupadd -r ctf && useradd -r -g ctf ctf && \
    chown -R ctf:ctf /ctf && \
    chmod 555 /start.sh && \
    chmod 444 /etc/xinetd.d/ctf && \
    chmod 444 /ctf/flag
CMD ["/bin/sh","/start.sh"]
