FROM python:3.10-slim

WORKDIR /home/project/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY elastic_net ./elastic_net
