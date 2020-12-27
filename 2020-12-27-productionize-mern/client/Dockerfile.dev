FROM node:14-slim

WORKDIR /usr/src/app

COPY ./package.json ./
COPY ./yarn.lock ./

RUN yarn install

COPY . .

ENV REACT_APP_BASE_URL=http://localhost:5000/api

EXPOSE 3000

CMD [ "yarn", "start" ]