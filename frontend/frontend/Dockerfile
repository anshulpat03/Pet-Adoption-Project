# Step 1: Use an official Node.js image as the base
FROM node:16-alpine AS build

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy package.json and package-lock.json
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the rest of the application code
COPY . .

# Step 6: Build the React app
RUN npm run build

# Step 7: Use a lightweight web server to serve the build
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Step 8: Expose port 80
EXPOSE 80

# Step 9: Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
