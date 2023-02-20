FROM python:3.10.10-alpine3.17
MAINTAINER pysga1996
WORKDIR /opt/spooky-user-service
RUN apk update && apk add --update --no-cache  \
    busybox-extras  \
    postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc zlib-dev musl-dev postgresql-dev
COPY ./requirements.txt /opt/spooky-user-service/requirements.txt
RUN pip install -r requirements.txt
COPY . /opt/spooky-user-service/
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
VOLUME /opt/spooky-user-service
EXPOSE 8000