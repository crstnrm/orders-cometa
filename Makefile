# The purpose of this file is to make it easy to run the project with all required services using docker.
# To see what commands are available please, run: make

.DEFAULT_GOAL := help

.PHONY: help

service = api

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: down ## run/recreate all services
	@docker-compose up

shell: ## run api container shell with ports enabled
	@docker-compose run --rm api bash

test: ## run all services and drop you into the api container shell
	@docker-compose run --rm --env PYTHONPATH=. api pytest

down: ## stop and remove docker containers
	@docker-compose down --remove-orphans

build: ## build the services
	@docker-compose build
