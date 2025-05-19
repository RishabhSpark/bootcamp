# Variables
APP_NAME=paper-metadata-app
CLI_ENTRY=main.py --help
API_MODULE=src.api.main:app
DOCKER_TAG=paper-metadata:latest

.PHONY: help run-cli run-api docker-build docker-cli docker-api

help:
	@echo "Available targets:"
	@echo "  docker-build   Build the Docker image"
	@echo "  docker-cli     Run the CLI inside Docker"
	@echo "  docker-api     Run the FastAPI server inside Docker"

docker-build:
	docker build -t $(DOCKER_TAG) .

docker-cli:
	docker run --rm -it $(DOCKER_TAG) python $(CLI_ENTRY)

docker-api:
	docker run -p 8000:8000 $(DOCKER_TAG) uvicorn $(API_MODULE) --host 0.0.0.0 --port 8000


# How to use docker-cli
# docker run --rm -it paper-metadata:latest python main.py

# How to use docker-api
# docker run -p 8000:8000 paper-metadata:latest uvicorn src.api.main:app --host 0.0.0.0 --port 8000