FROM python:3.10-slim-buster

ENV USER dreamhack
ENV PORT 8000
RUN adduser --disabled-password $USER -u 1337


RUN apt-get update -y && apt-get install -y python3-pip build-essential wget curl unzip

RUN pip install --upgrade pip

WORKDIR /app
COPY ./deploy .
COPY ./flag /

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["python3","app.py"]