# Pet Adoption Web Application

This project is a pet adoption web application that includes both a frontend (React) and a backend (Flask) that interact with each other. The frontend allows users to view and filter pets, while the backend provides an API to retrieve pet information stored in a SQLite database.

# Prerequisites

Docker installed on your machine
Project Structure
frontend: React application for displaying and interacting with pet data.
backend: Flask application that serves as the API, interacting with a SQLite database.

***We have completed up to requirements for Milestone 7. "Steel thread" is focused on a list of pets on the screen. We commented out most of our code, so we can work on future implementation to add more features. We separated the code we don't need for NOW, and all the codes that are curently running are dedicated to Home Page and Pets Page. We hope you understand!***

# Get Started with The Steps Below

# Clone the Repository
git clone git@github.uconn.edu:CSE2102-Fall24/cse2102-fall-Team21.git 

# Make Sure You Have 2 Terminals, One for Backend Docker, One for Frontend Docker

# Build and Run the Backend
1. Navigate to Backend Folder

   cd backend

2. Build the Docker image:

   docker build -t backendteam21 .

3. Run the Docker container:

   docker run -d -p 5000:5000 backendteam21

*Note* This will start the backend server on port 5000.

# Build and Run the Frontend

1. Navigate to Frontend Folder

   cd ../frontend

2. Download packages

   npm install react-router-dom

   npm install typescript --save-dev

3. Build the Docker image

   docker build -t frontendteam21 .

4. Run the Docker container

   docker run -d -p 5173:80 frontendteam21
