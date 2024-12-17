FROM ubuntu:20.04

RUN apt update \
    && apt install --assume-yes python3-pip libmariadb-dev

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
COPY WikiCrawler.py /usr/src/app

RUN pip3 install -r requirements.txt

CMD ["python3", "/usr/src/app/WikiCrawler.py"]
