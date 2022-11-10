FROM python:3.9-slim
ENV DEBIAN_FRONTEND=noninteractive
ENV DJANGO_SETTINGS_MODULE=eriell.settings

RUN apt-get update \
    && apt-get -y install build-essential \
    libpq-dev libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev zlib1g-dev lib32z1-dev


COPY ./requirements.txt /tmp/requirements/

RUN pip3 install --no-cache-dir -r /tmp/requirements/requirements.txt

RUN mkdir /code
WORKDIR /code
ADD . /code/
