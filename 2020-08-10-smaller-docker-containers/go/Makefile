run:
	docker run -i -d -p  8081:8081 go-naive

build-naive:
	docker build \
	-f $(CURDIR)/Dockerfile.naive \
	-t go-naive \
	.

build-alpine:
	docker build \
	-f $(CURDIR)/Dockerfile.alpine \
	-t go-alpine \
	.

build-alpine-multi:
	docker build \
	-f $(CURDIR)/Dockerfile.alpine-multi \
	-t go-alpine-multi \
	.
