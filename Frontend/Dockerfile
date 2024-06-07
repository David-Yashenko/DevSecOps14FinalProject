FROM node:hydrogen-alpine3.19

RUN sed -i 's/https/http/' /etc/apk/repositories

RUN apk update && apk add --no-cache ca-certificates

WORKDIR /usr/src/app

COPY package.json ./
COPY package-lock.json ./

RUN npm config set strict-ssl false
RUN npm config set registry http://registry.npmjs.org/

ENV NODE_OPTIONS=--openssl-legacy-provider

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
