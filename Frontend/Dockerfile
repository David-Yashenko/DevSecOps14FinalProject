FROM node:hydrogen-alpine3.19 as build

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
RUN npm run build

FROM nginx:alpine

COPY --from=build /usr/src/app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
