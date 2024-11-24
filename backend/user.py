"""
Manages user data and adoption progress for a pet adoption system
"""
import sqlite3

# users.py
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

def get_user_by_id(user_id):
    """Fetches a user by their ID."""
    conn = get_db_connection('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return dict(user) if user else None

def login_user(username, password):
    """Validates the username and password."""
    conn = get_db_connection('users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    if user:
        return dict(user)  # Return user details if login is successful
    return None  # Return None if credentials are invalid

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

def get_adoption_status(user_id):
    """Fetch the adoption status of a user."""
    conn = get_db_connection('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT adoption_status FROM users WHERE id = ?", (user_id,))
    status = cursor.fetchone()
    conn.close()
    return status["adoption_status"] if status else None

def add_form(data):
    """Store application form to database."""
    try:
        conn = get_db_connection('forms.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO forms (user_id, name, salary, housing, contact, pet_name) VALUES (?, ?, ?, ?,?)",
            (data.get("user_id"), data.get("name"), data.get("salary"), data.get("housing"),
            data.get("contact"), data.get("pet_name"))
        )
        conn.commit()
        return True
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False
    finally:
        conn.close()
