build:
	docker build -t express-hello-world .

run:
	docker run --rm -p 3000:3000 express-hello-world

run-dev:
	docker run \
		-p 3000:3000 \
		-p 9229:9229 \
		-v $(PWD):/usr/src/app \
		-v /usr/src/app/node_modules \
		hello-world-express nodemon --inspect=0.0.0.0:9229 server.js
