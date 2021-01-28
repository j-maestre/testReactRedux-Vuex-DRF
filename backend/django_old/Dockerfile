FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /config/requirements.txt
RUN mkdir /src;
WORKDIR /src 