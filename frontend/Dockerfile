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

EXPOSE 5173

CMD ["npm", "run", "dev"]
