FROM python:3.12

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml  ./

RUN poetry install

COPY . .