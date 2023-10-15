FROM python:latest

COPY . /easyliftover

RUN pip install ./easyliftover

RUN rm -rf /easyliftover