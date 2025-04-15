FROM node:18-alpine AS builder 
WORKDIR /src
COPY .  .
RUN npm install


FROM nginx:alpine
WORKDIR /usr/share/nginx/html
COPY --from=builder /src/App.js /usr/share/nginx/html
EXPOSE 8080
