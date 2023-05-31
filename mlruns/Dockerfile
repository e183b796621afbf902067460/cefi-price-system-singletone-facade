FROM python:3.10-slim

WORKDIR /home/project/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY logistic_regression.py ./logistic_regression.py
