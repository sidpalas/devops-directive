# Deploy MERN Application with Docker Compose

A few months ago I released a videos showing how to run a MERN stack application with Docker Compose.

The configuration shown there is great for development but not ready for production. There are a number of steps we need to take to get it ready to deploy.

- ✅ Restart:unless stopped
- ✅ Mount code into dev version to enable hot reloading w/ nodemon
- ✅ Remove volume mounts for code in production
- ✅ update urls as necessary (ENV vars for base url + mongo URI)
- ✅ Add authentication for DB (host w/ Atlas)
- ✅ Build production version of front end react app
- ✅ Serve front end files + set up SSL (set up Caddy)
- ✅ Create Digital Ocean VM
- ✅ Create HTTP/HTTPS/SSH firewall rule and attach
- ✅ Whitelist IP address of Server in Atlas
- TODO: Add authentication to the API (Separate Video)

