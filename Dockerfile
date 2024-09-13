FROM python:3

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .
