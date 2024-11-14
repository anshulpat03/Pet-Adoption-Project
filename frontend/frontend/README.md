Pet Adoption Web Application
This project is a pet adoption web application that includes both a frontend (React) and a backend (Flask) that interact with each other. The frontend allows users to view and filter pets, while the backend provides an API to retrieve pet information stored in a SQLite database.

Prerequisites
Docker installed on your machine
Project Structure
frontend: React application for displaying and interacting with pet data.
backend: Flask application that serves as the API, interacting with a SQLite database.
Getting Started
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/pet-adoption-app.git
cd pet-adoption-app
2. Build and Run the Backend
Navigate to the backend folder:

bash
Copy code
cd backend
Create a Dockerfile for the Backend (if not already present):

dockerfile
Copy code
# Dockerfile for backend

# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Step 4: Copy the rest of the application code
COPY . .

# Step 5: Expose port 5000 for the Flask API
EXPOSE 5000

# Step 6: Start the Flask server
CMD ["python3", "main.py"]
Build the Docker image:

bash
Copy code
docker build -t pet-backend .
Run the Docker container:

bash
Copy code
docker run -d -p 5000:5000 --name pet-backend pet-backend
This will start the backend server on port 5000.

3. Build and Run the Frontend
Navigate to the frontend folder:

bash
Copy code
cd ../frontend
Create a Dockerfile for the Frontend (if not already present):

dockerfile
Copy code
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
Build the Docker image:

bash
Copy code
docker build -t pet-frontend .
Run the Docker container:

bash
Copy code
docker run -d -p 5173:80 --name pet-frontend pet-frontend
This will start the frontend server on port 5173.

4. Verify the Setup
Frontend: Open a browser and go to http://localhost:5173 to view the pet adoption page.
Backend: The backend API is available at http://localhost:5000/pets for the list of pets.
5. Docker Compose (Optional)
To simplify running both services together, you can use Docker Compose. Create a docker-compose.yml file in the root of your project:

yaml
Copy code
version: '3'
services:
  backend:
    build: ./backend
    container_name: pet-backend
    ports:
      - "5000:5000"
  frontend:
    build: ./frontend
    container_name: pet-frontend
    ports:
      - "5173:80"
    depends_on:
      - backend
Then, run both containers with:

bash
Copy code
docker-compose up -d
This will start both the backend and frontend services. You can stop them with:

bash
Copy code
docker-compose down
Notes
API URL in Frontend: Ensure the API URL in the frontend code (e.g., http://localhost:5000/pets) matches the backend URL and port.
Database Initialization: The backend automatically initializes the SQLite database and creates sample pet data on startup.
Troubleshooting
Port Conflicts: If you encounter port conflicts, make sure ports 5000 (backend) and 5173 (frontend) are available, or change them in the Docker and Docker Compose configurations.
CORS Issues: CORS is enabled in the backend for development purposes. If you encounter CORS errors, ensure the flask_cors library is correctly configured in the backend.