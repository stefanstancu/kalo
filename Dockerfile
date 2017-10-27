FROM python:alpine

ADD ./app /var/www/app

WORKDIR /var/www/app

RUN apk --update add linux-headers musl-dev gcc postgresql-dev

RUN pip3 install -r requirements.txt

CMD ["flask","run"]
