FROM node AS build_stage

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

FROM nginx:alpine AS host

COPY --from=build_stage /app/build /usr/share/nginx/html

