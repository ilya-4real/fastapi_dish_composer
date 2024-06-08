##  Recipe composer
ready to go API for storing, creating, and generating random recipes.

> ⚠️ project curently is under active developing

## Start project for dev purposes

- install dependencies
 ~~~ bash
 poetry install --no-root # to install only deps
 ~~~

- raise mongo storage
~~~ bash
make storages
~~~

- run uvicorn test server
~~~ bash
uvicorn fastapi_proj.application.main:app --reload
~~~

Everything is ready

> There is configured pre-commit hook which will lint the code before commit. Also there is configuration for `ruff` in `pyproject.toml`. So you can use it to check code validity.



