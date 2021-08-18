FROM node:14

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json ./
COPY yarn.lock ./
RUN yarn

# Copy in the source code
COPY . .

# Don't use root user
USER node

# Expose Port
EXPOSE 3000

# Run the app
CMD ["node", "server.js"]