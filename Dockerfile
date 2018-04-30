FROM python:alpine

COPY ./app /var/www/app

WORKDIR /var/www/app

RUN apk --update add linux-headers musl-dev gcc postgresql-dev

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask","run", "--host=0.0.0.0"]
