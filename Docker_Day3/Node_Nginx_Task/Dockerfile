# Stage 1: Build React app
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN npm install

# Copy app source
COPY . .

# Build the React app
RUN npm run build

# Stage 2: Serve app with nginx
FROM nginx:alpine

# Copy build output to nginx html folder
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

