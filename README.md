# Pet-Adoption-Project-cse2102-fall-2024 

A Team Collaboration Project
Anshul Patwardhan



Overview:
    This project was originally developed as part of a team effort in the 2024 Fall Semester at the University of Connecticut. It includes the back and frontend of a website which imitates a real Pet Adoption Website.

    The repository hosted here is a copy of our collective work brought over onto my personal GitHub account for portfolio purposes. The original project was developed in a private repo under the university's GitHub server, by a team of four members including myself.



How to Run the Project Locally:
    Backend:
        1. cd into backend (cd backend)
        2. Run the backend (python3 main.py)
    Frontend:
        1. While backend is running, cd into frontend in a new terminal (cd frontend)
        2. run npm install in this new terminal while cd into frontend (npm install)
        3. Run the frontend (npm run dev)
        4. ctrl + click on the Local or Network links to open the site

            (To access Adoption Form, use the test username "John Doe" and the password "testpassword1")



Features:
    1. The Homepage (accessed by clicking the circular logo in the top left) which states our "mission statement" and clear buttons to access all the different pages for our site.
    
    2. A "User Login" page, which unless correctly signed into restricts access to parts of the website like the "Adoption Form."

    3. A "Pets" page (same as the "Browse Pets" button on the home screen), which lists all pets available for adoption

    4. An "Admin Dashboard" page, which simulates the view of our website from the eyes of an adoption center, which is using this site to streamline the adoption process online. It allows them to see all current applicants, their names, emails, and status, and adoption forms. In addition, it allows them to see all current pets, and directly edit the list, or edit pet information (such as Name, Breed, Age, and Description)

    5. An "Adoption Form" which can only be accessed once a user is logged in.

    6. A "Contact Us" popup which displays the Agency's contact information.

    7. A "User Dashboard" which allows the user to see their entered information.



Acknowledgements - this project was developed collectively by:
    - Anny Zheng
    - Divya S Patel
    - Jiahui Jennifer Weng Wu
    - Anshul A Patwardhan



Technologies Used: 
    React - Frontend
    Python Flask - backend / API
    SQLite - Database
