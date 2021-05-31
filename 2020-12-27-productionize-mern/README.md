# Deploy MERN Application with Docker Compose

Live stream: https://youtu.be/DftsReyhz2Q

A few months ago I released a videos showing how to run a MERN stack application with Docker Compose: [../2020-08-31-docker-compose](../2020-08-31-docker-compose).

The configuration shown there is great for development but not ready for production. There are a number of steps we need to take to get it ready to deploy.

- ✅ Mount code into dev version to enable hot reloading (make sure not to mount in node_modules)
- ✅ Restart:unless stopped
- ✅ Remove volume mounts for code in production
- ✅ Environment specific urls (ENV vars for base url + mongo URI)
- ✅ Add authentication for DB 
- ✅ Move DB to MongoDB Atlas
- ✅ Build production version of front end react app
- ✅ Serve static front end files from file server container
- ✅ Set up SSL (using Caddy)
- ✅ Create Digital Ocean VM
- ✅ Create HTTP/HTTPS/SSH firewall rule and attach to VM
- ✅ Whitelist IP address of Server in Atlas
- TODO: Add authentication to the API (Separate Video)

