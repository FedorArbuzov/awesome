FROM python:3.7-alpine

RUN pip install pipenv

RUN pip install flask

WORKDIR /app


EXPOSE 5000

ENTRYPOINT python server.py