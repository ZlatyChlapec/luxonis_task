FROM node:21-slim as build

WORKDIR /app
COPY ./package.json ./yarn.lock ./
RUN yarn install

COPY . .
RUN yarn prod-build

FROM nginx:1.25-alpine as run

WORKDIR /usr/share/nginx/html
COPY --from=build /app/dist/. .
