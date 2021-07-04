# Use an official node runtime as a parent image
FROM node:12.18.3-alpine3.9

WORKDIR /app/

# Install dependencies
COPY package.json yarn.lock /app/

# install dependencies and avoid `node-gyp rebuild` errors
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install \
    && apk del .gyp


# Add rest of the client code
COPY . /app/

EXPOSE 3000

CMD npm start
