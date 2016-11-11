FROM ubuntu:14.04

RUN apt-get update -y
RUN apt-get install -y python python-dev libssl-dev libffi-dev
RUN apt-get install -y libpq-dev

RUN apt-get install -y wget
RUN apt-get install -y make
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

RUN apt-get install -y python-psycopg2

ADD . /src
WORKDIR /src

RUN pip install -r /src/requirements.txt

EXPOSE 8080
CMD ["python", "/src/app_db.py", "-p 8080"]
