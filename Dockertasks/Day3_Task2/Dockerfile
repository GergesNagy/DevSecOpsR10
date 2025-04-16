FROM node:alpine AS first
WORKDIR /app
RUN npx create-react-app .
COPY ./App.js src/App.js
COPY ./package.json ./
# RUN npm install
# COPY . .
RUN npm run build


FROM nginx:alpine
COPY --from=first /app/build /usr/share/nginx/html

