FROM python:3 AS python3

WORKDIR /python

COPY . .

RUN pip install -r requirements.txt

FROM python:2 as python2

WORKDIR /python

COPY . .

RUN pip install -r requirements.txt
