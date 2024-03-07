from python:3.12

workdir /code
run pip install poetry

copy poetry.lock /code
copy pyproject.toml /code

run poetry config virtualenvs.create false
run poetry install

copy . /code


cmd uvicorn main:app --host 0.0.0.0 --port 80
