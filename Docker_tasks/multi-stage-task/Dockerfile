FROM node AS build

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build 

#-----------------------------STAGE 2

FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build /app/build /usr/share/nginx/html
