FROM python:3.12-alpine
LABEL MAINTAINER="Tom Freudenberg <th.freudenberg@gmail.com>"
ENV PS1="\[\e[0;33m\]\(> spiral <\) \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "
ENV SPIRAL_ENV=prod

WORKDIR /app
COPY . /app
COPY .alpine/.profile /root
COPY .alpine/.screenrc /root

RUN apk add --update --no-cache \
    tzdata \
    linux-headers \
    build-base \
    cmake \
    gcc \
    g++ \
    git \
    screen \
    erlang \
    rabbitmq-server \
    && ln -s /usr/share/zoneinfo/UTC /etc/localtime \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -e . \
    && pip install --no-cache-dir -e .[dev]

WORKDIR /app
ENTRYPOINT ["ash", "-l"]
