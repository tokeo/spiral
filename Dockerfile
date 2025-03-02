FROM python:3.12-alpine
LABEL MAINTAINER=" <>"
ENV PS1="\[\e[0;33m\]\(> spiral <\) \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /app
COPY . /app
RUN apk add --update --no-cache \
    linux-headers \
    build-base \
    cmake \
    gcc \
    g++ \
    git \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -e .
WORKDIR /
ENTRYPOINT ["spiral"]
