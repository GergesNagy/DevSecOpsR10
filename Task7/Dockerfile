FROM node AS build

WORKDIR /app

COPY . . 


RUN npm install

RUN npm run build

####################
FROM nginx:latest

WORKDIR /app

COPY --from=build /app/build .


