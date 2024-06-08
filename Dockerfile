FROM python:3.12

WORKDIR /code
RUN pip install poetry

COPY poetry.lock /code
COPY pyproject.toml /code

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /code


CMD uvicorn main:app --host 0.0.0.0 --port 80
