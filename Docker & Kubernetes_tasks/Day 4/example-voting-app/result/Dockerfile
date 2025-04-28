# Use the official Node.js LTS image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker cache
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application
COPY . .

# Build the app if necessary (uncomment if using a build step like Webpack)
# RUN npm run build

# Expose the port used by the app
EXPOSE 80

# Start the app
CMD ["node", "server.js"]