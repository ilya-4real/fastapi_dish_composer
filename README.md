##  Recipe composer
ready to go API for storing, creating, and generating random recipes.

## Navigation
- [Used tech](#used-tech)
- [Architecture and patterns](#architecture-and-patterns)
- [TODO](#todo)
- [Start project for dev purposes](#start-project-for-dev-purposes)
- [Run project in production environment](#run-project-in-production-environment)



## Used tech
- `FastAPI` - as python web framework
- `mongodb` - as data storage
- `Docker/ Docker compose` - as container runtime
- `punq` - as DI framework 

## Architecture and patterns
- `Clean architecture by uncle Bob` - as a mindset for building this application
- Whole application is divided in `layers` to make business logic and technology specific code low coupled
- `Domain layer` - contains domain specific entities
- `Logic layer` - contains business specific logic or as it is called use cases
- `Infra layer` - contains contains code that provides different infrastructure like repositories and DI container
- `Application layer` - contains framework specific code

- `Mediator` - in this project is not a classic implementation but something in the middle between observer and event bus

## Contribution 
- Keep in mind that it is better to use DI than not to use
- Keep same naming style
- Use ruff as linter (configuration is in pyproject.toml)

## TODO
1. `Tests` - are very **necessary**
2. Implementation of whole CRUD for recipes block is **needed**
3. And a lot of things in the frontend

## Start project for dev purposes

- install dependencies
 ~~~ bash
 poetry install --no-root # to install only deps
 ~~~

- raise mongo storage
~~~ bash
make storages
~~~

- provide environment variables in file named `.env` in the root of the project:
~~~
MONGO_USERNAME=admin
MONGO_PASSWORD=pass1234
MONGO_PORT=27017
MONGO_HOST=localhost
CORS_ORIGINS='["www.example.com"]'
MODE=DEV
~~~

- run uvicorn test server
~~~ bash
uvicorn fastapi_proj.application.main:app --reload
~~~

Everything is ready

> There is configured pre-commit hook which will lint the code before commit. Also there is configuration for `ruff` in `pyproject.toml`. So you can use it to check code validity.

## Run project in production environment

- pull image from dockerhub:

~~~ bash
docker pull ilya4r/recipe-builder:backend
~~~

- run image with provided environment variables:

~~~ bash
docker run --name backend \
-p 8000:8000 --network mongonet \
-e MONGO_PORT=27017 -e MONGO_HOST=localhost \
-e MONGO_USERNAME=admin -e MONGO_PASSWORD=superpassword  -d \
-e REDIS_HOST=localhost -e REDIS_PORT=6379 \
-e CORS_ORIGINS='["www.example.com"]' ilya4r/recipe-builder:backend
~~~




