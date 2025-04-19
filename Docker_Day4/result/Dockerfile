FROM node:alpine

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

# Change port number from 4000 to 80
ENV PORT=80

ENTRYPOINT ["npm", "start"]
