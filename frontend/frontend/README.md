Pet Adoption Web Application
This project is a pet adoption web application that includes both a frontend (React) and a backend (Flask) that interact with each other. The frontend allows users to view and filter pets, while the backend provides an API to retrieve pet information stored in a SQLite database.

Prerequisites
Docker installed on your machine
Project Structure
frontend: React application for displaying and interacting with pet data.
backend: Flask application that serves as the API, interacting with a SQLite database.

Progress So Far
***We have completed up to requirements for Milestone 7. "Steel thread" is focused on a list of pets on the screen. We commented out most of our code, so we can work on future implementation to add more features. We separated the code we don't need for NOW, and all the codes that are curently running are dedicated to Home Page and Pets Page. We hope you understand!***

Get Started with The Steps Below

Clone the Repository
git clone https://github.com/your-username/pet-adoption-app.git
cd pet-adoption-app

Build and Run the Backend
1. Navigate to Backend Folder
cd backend

2. Build the Docker image:
docker build -t pet-backend .

3. Run the Docker container:
docker run -d -p 5000:5000 --name pet-backend pet-backend
*Note* This will start the backend server on port 5000.

Build and Run the Frontend
1. Navigate to Frontend Folder
cd ../frontend

2. Build the Docker image
docker build -t pet-frontend .

3. Run the Docker container
docker run -d -p 5173:80 --name pet-frontend pet-frontend

4. In Case You Don't Find Dockerfile for Frontend Code, Create A Dockefile + Do This Before Step 2
# Dockerfile for frontend

# Step 1: Use an official Node.js image as the base image
FROM node:16-alpine AS build

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Step 4: Copy the rest of the application code
COPY . .

# Step 5: Build the React app
RUN npm run build

# Step 6: Use Nginx to serve the built app
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Step 7: Expose port 80
EXPOSE 80

# Step 8: Start Nginx
CMD ["nginx", "-g", "daemon off;"]
