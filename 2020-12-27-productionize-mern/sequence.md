**Part 1: Dockerize**
1) Run baseline application
```
yarn start
yarn start
brew services start mongodb-community@4.4
```

2) Move Mongo to container

`docker run -p 27017:27017 mongo:4.4-bionic`

3) Dockerize react client [Dockerfile](./client/Dockerfile.dev)
4) Dockerize api server [Dockerfile](./server/Dockerfile)
5) Set up docker compose [docker-compose.yml](./docker-compose-dev.yml)
6) Enable hot reloading by mounting in src

**Part 2: Productionize**
1) add restart: unless-stopped
2) Break out separate docker-compose files
3) Move DB to Atlas
4) Update client Dockerfile to build production version
5) Use Caddy to serve front end files
6) Parameterize connection strings
7) Split local and production configurations

**Part 3: Deployment**
1) Create Digital Ocean VM
2) Configure DNS
3) Configure network access in Atlas
4) Configure Caddy
5) Deploy!

