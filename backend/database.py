"""
Initialization file for the databases
"""
import sqlite3
import os

def get_db_connection(db_name):
    """
    Establishes a connection to the database and enables dictionary-like row access.
    """
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row  #
                                 # Allows dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database {db_name}: {e}")
        return None

def init_user_db():
    """
    Initializes the user database by creating the 'users' table and adding sample users.
    """
    db_name = 'users.db'
    if os.path.exists(db_name):
        os.remove(db_name)

    conn = get_db_connection(db_name)
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)'
                )
            # Inserting three sample users
            users = [
                ('John Doe', 'johndoe@example.com', 'testpassword1'),
                ('Jane Smith', 'janesmith@example.com', 'testpassword2'),
                ('Alice Johnson', 'alicej@example.com', 'testpassword3')
            ]
            cursor.executemany(
                'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',users
                )
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing user database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to initialize user database due to connection error.")

def init_pets_db():
    """Initialize the databse for pets"""
    db_name = 'pets.db'
    if os.path.exists(db_name):
        os.remove(db_name)
    
    conn = get_db_connection(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT,
            age INTEGER,
            description TEXT,
            image TEXT
        )
    ''')

    # Insert sample data
    sample_pets = [
        ('Bella', 'Labrador', 3, 'Friendly and energetic.', '/images/Labrador.png'),
        ('Max', 'Golden Retriever', 5, 'Loyal and calm.', '/images/Golden Retriever.png'),
        ('Lucy', 'Bulldog', 2, 'Playful and loving.', '/images/Bulldog.png')
    ]
    cursor.executemany(
        'INSERT INTO pets (name, breed, age, description, image) VALUES (?, ?, ?, ?, ?)',
        sample_pets)
    conn.commit()
    conn.close()

def init_adoption_progress_db():
    """
    Initializes the adoption progress database for tracking user adoption progress.
    """
    db_name = 'adoption_progress.db'
    if os.path.exists(db_name):
        os.remove(db_name)

    conn = get_db_connection(db_name)
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
               'CREATE TABLE IF NOT EXISTS adoption_progress (id INTEGER PRIMARY KEY, user_id INTEGER, pet_id INTEGER, status TEXT NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(pet_id) REFERENCES pets(id))'
                )
            # Inserting some sample adoption progress data
            adoption_data = [
                (1, 1, "In Progress"),
                (2, 2, "Completed"),
                (3, 3, "Pending")
            ]
            cursor.executemany('INSERT INTO adoption_progress (user_id, pet_id, status) VALUES (?, ?, ?)', adoption_data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing adoption progress database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to initialize adoption progress database due to connection error.")

def initialize_all():
    """
    Calls all individual initialization functions to set up the databases.
    """
    init_user_db()
    init_pets_db()
    init_adoption_progress_db()
    print("All databases initialized.")

# Running this file will initialize the databases.
if __name__ == '__main__':
    initialize_all()
