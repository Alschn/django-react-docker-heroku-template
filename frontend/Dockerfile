# Use an official node runtime as a parent image - Build stage
FROM node:14.17.5-alpine as build-image

WORKDIR /app/frontend

COPY package.json .

# install dependencies and avoid `node-gyp rebuild` errors
RUN \
    apk add --virtual .gyp python make g++ && \
    yarn install && \
    apk del .gyp && \
    yarn cache clean --all

# Use an official node runtime as a parent image - Runtime
FROM node:14.17.5-alpine as runtime

WORKDIR /app/frontend

# copy node_modules from build stage
COPY --from=build-image /app/frontend/node_modules /app/frontend/node_modules

# copy rest of source code
COPY . .

RUN apk add bash

EXPOSE 3000

CMD ["yarn", "start"]
