FROM ubuntu:latest AS builder
RUN apt update
RUN apt install -y git

WORKDIR /app
RUN git clone https://github.com/andru-oca/anderson-presentacion.git

FROM nginx:stable-alpine3.17-slim

WORKDIR /app
COPY --from=builder  /app/anderson-presentacion /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80