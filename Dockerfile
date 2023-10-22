FROM ubuntu:latest

WORKDIR /home
RUN apt update && apt install -y git
RUN git clone https://github.com/ashwin347/athenaeum
