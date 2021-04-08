# NODE
build-node-naive:
	docker build -t 00-node-naive -f ./node/Dockerfile.naive ./node

build-node-slim:
	docker build -t 01-node-slim -f ./node/Dockerfile.slim ./node

build-node-alpine:
	docker build -t 02-node-alpine -f ./node/Dockerfile.alpine ./node

build-all-node:
	$(MAKE) build-node-naive
	$(MAKE) build-node-slim
	$(MAKE) build-node-alpine

# GO
build-go-naive:
	docker build -t 03-go-naive -f ./go/Dockerfile.naive	./go

build-go-multi:
	docker build -t 04-go-alpine -f ./go/Dockerfile.alpine-multi ./go

build-go-scratch:
	docker build -t 05-go-scratch -f ./go/Dockerfile.scratch ./go

build-all-go:
	$(MAKE) build-go-naive
	$(MAKE) build-go-multi
	$(MAKE) build-go-scratch


# C
build-c:
	docker build -t c-scratch ./c

# ASM
build-asm:
	docker build -t 06-asm-scratch ./asm

build-all:
	$(MAKE) build-all-node
	$(MAKE) build-all-go
	$(MAKE) build-c
	$(MAKE) build-asm

run:
	docker run -d --rm -p 8081:8081 --name server go-scratch

stop:
	docker kill server

list-image-sizes:
	docker images --format \
		"{{.ID}}\t{{.Size}}\t{{.Repository}}" | \
		sort -k 3 -h | \
		grep 'node-\|go-\|c-\|asm-'

