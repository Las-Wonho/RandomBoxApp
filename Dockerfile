FROM python:3.7

COPY . .

RUN pip install numpy && pip install flask