# Use official Node.js LTS image
FROM node:20-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all source files to the working directory
COPY . .

# Run the server
CMD ["node", "server.js"]

#docker run -p 8081:4000 result-compose