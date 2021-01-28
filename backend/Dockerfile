FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# FROM python:3.6-alpine
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /config
# ADD /config/requirements.txt /config/
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN pip install -r /config/requirements.txt
# RUN mkdir /src;
# WORKDIR /src 

