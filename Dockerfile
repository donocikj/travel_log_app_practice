FROM python:3.10-slim-bullseye AS be_build

ENV PIP_DISABLE_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

FROM node:19-bullseye-slim AS fe_build

WORKDIR /code

COPY . .

WORKDIR /code/traveller_log_fe
RUN npm install



