#Ensure the loader service's Dockerfile uses a base image that includes Python.

FROM python:3.9-slim

RUN apt update \
    && apt install --assume-yes python3-pip libmariadb-dev

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
COPY DataLoader.py /usr/src/app

RUN pip3 install -r requirements.txt

CMD ["python3", "/usr/src/app/DataLoader.py"]