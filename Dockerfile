FROM python:3.9.12
MAINTAINER pysga1996
WORKDIR /opt/spooky-user-service
COPY ./requirements.txt /opt/spooky-user-service
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
VOLUME /opt/spooky-user-service
EXPOSE 8000