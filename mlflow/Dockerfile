FROM python:3.10-slim

WORKDIR /home/project/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY exp ./exp
