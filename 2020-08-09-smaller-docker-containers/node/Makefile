run:
	docker run -i -d -p 8080:8080 node-naive 

# 918MB
build-naive:
	docker build \
	-f $(CURDIR)/Dockerfile.naive \
	-t node-naive \
	.

# 142MB
build-slim:
	docker build \
	-f $(CURDIR)/Dockerfile.slim \
	-t node-slim \
	.

# 89.3MB
build-alpine:
	docker build \
	-f $(CURDIR)/Dockerfile.alpine \
	-t node-alpine \
	.
