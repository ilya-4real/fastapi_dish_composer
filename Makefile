DC = docker compose
STORAGES_FILE = compose-files/storages.yaml
ENV_FILE = .env


.PHONY: storages
storages: 
	${DC} -f ${STORAGES_FILE} --env-file ${ENV_FILE} up -d


.PHONY: storages-down
storages-down: 
	${DC} -f ${STORAGES_FILE} down

.PHONY: app-dev
app-dev: 
	uvicorn fastapi_proj.application.main:app --reload


