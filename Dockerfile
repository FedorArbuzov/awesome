FROM python:3.7-alpine



RUN apk add postgresql-dev

RUN apk add --no-cache --virtual .build-deps g++ make jpeg-dev && \
    pip install sanic && \
    apk del .build-deps

RUN pip install xlrd

WORKDIR /app

RUN touch ~/.netrc

EXPOSE 5000

CMD exec gunicorn -w 4 -t 2000 --max-requests 1000 -b 0.0.0.0:5000 server:app --worker-class sanic.worker.GunicornWorker