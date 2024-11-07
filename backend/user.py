"""
Manages user data and adoption progress for a pet adoption system
"""
import sqlite3

# users.py
users2 = [
    {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "adoption_progress": [
            {"pet_id": 1, "status": "Pending"}
        ]
    },
    {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com",
        "adoption_progress": [
            {"pet_id": 2, "status": "Approved"}
        ]
    },
    {
        "id": 3,
        "name": "Charlie",
        "email": "charlie@example.com",
        "adoption_progress": [
            {"pet_id": 3, "status": "Denied"}
        ]
    }
]
def get_db_connection(name):
    """Get connection to database"""
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row  # Optional, allows dictionary-like access to rows
    return conn

def fetch_users_from_db():
    "Fetch users from the database"
    conn = get_db_connection('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users") # pylint : diable=w0621
    users = cursor.fetchall() # pylint: disable=W0621
    conn.close() # pylint: disable=W0621
    return users # pylint: disable=W0621

# Initialize users
users = fetch_users_from_db()

def get_user_by_id(user_id):
    """Fetches a user by their ID."""
    conn = get_db_connection('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None
    #for user in users:
        #if user["id"] == user_id:
            #return user
    #return None

def register_user(user_data):
    """Registers a new user."""
    conn = get_db_connection('users.db')
    cursor = conn.cursor()

    # Insert new user into the database
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (user_data.get("name"), user_data.get("email"))
    )

    conn.commit()

    # get the id of the new user register
    new_id = cursor.lastrowid
    conn.close()

    return {
        "id": new_id,
        "name": user_data.get("name"),
        "email": user_data.get("email")
    }

def get_user_adoption_progress(user_id):
    """Retrieve a user's adoption progress."""
    user = get_user_by_id(user_id)
    if user:
        return user.get("adoption_progress", [])
    return {"error": "User not found"}
