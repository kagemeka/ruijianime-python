FROM ubuntu:20.04 


SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ARG GECKO_VER=0.29.0
RUN \
  apt update \
  && apt install -y \
  python3-pip \
  wget \
  zip \
  && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VER}/geckodriver-v${GECKO_VER}-linux64.tar.gz \
  && tar -C /usr/bin/ -xvzf geckodriver*.tar.gz \
  && rm geckodriver* \
  && chmod +x /usr/bin/geckodriver

COPY py/requirements.txt .
RUN \
  pip install -r requirements.txt \
  && rm requirements.txt