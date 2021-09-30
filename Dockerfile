# syntax=docker/dockerfile:1

FROM python:3.9.7-slim-bullseye

WORKDIR /CmyPlot

COPY requirements.txt requirements.txt
COPY setup.cfg setup.cfg
COPY setup.py setup.py
COPY ./src/plotting ./src/plotting

RUN pip3 install -r requirements.txt

RUN pip install -e .

COPY ./src/plotting .

CMD ["python3", "-m", "index", "--host=0.0.0.0"]