# Use an official node runtime as a parent image - Build stage
FROM node:16.16.0-alpine as build-image

WORKDIR /app/frontend

COPY package.json yarn.lock /app/frontend/

# install dependencies and avoid `node-gyp rebuild` errors
RUN \
    apk add --virtual .gyp python3 make g++ && \
    yarn install && \
    apk del .gyp && \
    yarn cache clean --all

# Use an official node runtime as a parent image - Runtime
FROM node:16.16.0-alpine as runtime

WORKDIR /app/frontend

# copy node_modules from build stage
COPY --from=build-image /app/frontend/node_modules /app/frontend/node_modules

# copy rest of source code
COPY . .

RUN apk add bash

EXPOSE 3000

CMD ["yarn", "dev", "--host"]
