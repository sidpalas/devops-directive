# Developing with Docker

Video: https://youtu.be/5JQlFK6MdVQ

## Developer Experience issues:

### Slow iteration:

Rebuilding the image is slow. How can we use something like nodemon to watch for file changes? 

Yes, but we must use volume mounts such that changes to the host filesystem are reflected inside the container:

  - Install nodemon globally in Dockerfile (`RUN yarn global add nodemon`)
  - Mount the source code into the container at runtime (`-v $(PWD):/usr/src/app`)
  - Use an empty mount to avoid mounting the node_modules directory (`-v /usr/src/app/node_modules` 
  - Override cmd at runtime (`docker run... nodemon server.js`)

### Debugging:
  
Do normal debugging tools work?

Yes, but we must forward the necessary port and have the debugger listen on `0.0.0.0`:

  - Use the inspect flag at runtime with explicit address (`--inspect=0.0.0.0:9229`)
  - Add port forward for the proper port (`-p 9229:9229`)
  - Connect to debugger like normal (one option `chrome://about:inspect`)

### Lots of command line flags + complexity 

Now the docker run commands are super complex. How can we deal with that?

Use docker compose to encode the configuration in a yaml file! 

