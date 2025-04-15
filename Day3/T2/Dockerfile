FROM node:latest AS builder
WORKDIR /app
RUN npx create-react-app simple-react-app
COPY ./App.js /app/simple-react-app/src/App.js
COPY ./package.json /app/simple-react-app/package.json
WORKDIR /app/simple-react-app
RUN ["npm", "run", "build"]

FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/simple-react-app/build /usr/share/nginx/html
