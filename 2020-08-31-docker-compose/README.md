# MERN Docker Compose Demo

I followed [this tutorial](https://medium.com/swlh/how-to-create-your-first-mern-mongodb-express-js-react-js-and-node-js-stack-7e8b20463e66) to get basic app working.

I then containerized the api server and react client and created docker-compose to connect them.

---

Run `make build` from root to build containers
Run `make run` from root to run containers with docker-compose

---

**NOTE:** This is a development configuration where the react app is being served by a separate container. We would also want to create a production version where we build a static version of the react site and serve it with something like nginx.
