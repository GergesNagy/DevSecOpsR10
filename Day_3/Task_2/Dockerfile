# Build Stage
FROM node:latest AS build_stage

WORKDIR /app

# Create React app
RUN npx create-react-app .

# Overwrite default App component and package.json
COPY ./App.js ./src/App.js
COPY ./package.json ./package.json

# Build the React app
RUN npm run build

# Deploy Stage
FROM nginx:latest AS deploy_stage

# Copy build output to NGINX's web directory
COPY --from=build_stage /app/build /usr/share/nginx/html

# Start NGINX in the foreground to keep the container alive
CMD ["nginx", "-g", "daemon off;"]
