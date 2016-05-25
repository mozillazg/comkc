FROM python:3

RUN mkdir /opt/comkc/
COPY ./requirements*.txt ./
RUN pip install -r requirements.txt

WORKDIR /opt/comkc/
COPY ./ /opt/comkc/
RUN pip install .
