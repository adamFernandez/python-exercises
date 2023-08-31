# Get the current directory name as the default container and image names
CURRENT_DIR := $(shell basename $(CURDIR))
export IMAGE_NAME ?= $(CURRENT_DIR)
export CONTAINER_NAME ?= $(CURRENT_DIR)

build:
	@docker build -t $(IMAGE_NAME) --rm .
# docker run -it --rm $(IMAGE_NAME) /bin/bash

run: build
	clear
	@docker-compose run --rm app

exec:
	@docker exec -it $(CONTAINER_NAME) /bin/bash

stop:
	@docker-compose down

clean:
	@docker stop $(CONTAINER_NAME) || true
	@docker rm $(CONTAINER_NAME) || true
	@docker rmi $(IMAGE_NAME) || true
