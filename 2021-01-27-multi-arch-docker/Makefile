login:
	docker login

list-builders:
	docker buildx ls

initialize-builder:
	docker buildx create --name mybuilder
	docker buildx use mybuilder
	docker buildx inspect --boostrap

build:
	docker buildx build \
		--platform linux/amd64,linux/arm64,linux/arm/v7 \
		-t sidpalas/multi-arch-test:latest \
		--push \
		.

CONTAINER_NAME:=multi-arch-test
run:
	docker run -i -d --rm \
		-p 8080:8080 \
		--name $(CONTAINER_NAME) \
		sidpalas/multi-arch-test

ARM_SHA?=660432aec93b84c61d24541e5cf135491829df01ac900a20de325f8726f6118c
run-arm:
	docker run -i -d --rm \
		-p 8080:8080 \
		--name $(CONTAINER_NAME) \
		sidpalas/multi-arch-test@sha256:$(ARM_SHA)

stop:
	docker stop $(CONTAINER_NAME)

inspect:
	docker buildx imagetools inspect sidpalas/multi-arch-test:latest
