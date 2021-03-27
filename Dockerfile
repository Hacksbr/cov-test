FROM python:3.9.2-slim-buster

ENV PYTHONUNBUFFERED 1

# Install prerequisites
RUN apt-get update && apt-get install -y curl

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
