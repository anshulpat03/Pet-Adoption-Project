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
        conn.row_factory = sqlite3.Row
                                 # Allows dictionary-like access to rows
        return conn
    except sqlite3.Error as e: # pylint: disable=C0103
        print(f"Error connecting to database {db_name}: {e}")
        return None

def init_user_db():
    """initialize databse for users"""
    db_name = 'users.db'
    # if os.path.exists(db_name):
    #     os.remove(db_name)
    conn = get_db_connection(db_name)
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS users ('
                'id INTEGER PRIMARY KEY, '
                'username TEXT NOT NULL, '
                'email TEXT NOT NULL UNIQUE, '
                'password TEXT NOT NULL, '
                'adoption_status TEXT DEFAULT "pending")'  # New column
            )
            # Inserting sample users
            users = [
                ('John Doe', 'johndoe@example.com', 'testpassword1', 'pending'),
                ('Jane Smith', 'janesmith@example.com', 'testpassword2', 'accepted'),
                ('Alice Johnson', 'alicej@example.com', 'testpassword3', 'denied')
            ]
            cursor.executemany(
                'INSERT INTO users (username, email, password, adoption_status) VALUES (?, ?, ?, ?)',
                users
            )
            conn.commit()
        except sqlite3.Error as e: # pylint: disable=W0621
            print(f"Error initializing user database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to initialize user database due to connection error.")

def init_pets_db():
    """Initialize the databse for pets"""
    db_name = 'pets.db'
    
    conn = get_db_connection(db_name)
    if conn is not None:
        try:
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
        except sqlite3.Error as e: # pylint: disable=W0621
            print(f"Error initializing user database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to initialize pets database due to connection error.")
    
def init_form_db():
    """Initialize the databse for application form"""
    db_name = 'forms.db'
    # if os.path.exists(db_name):
    #     os.remove(db_name)
    conn = get_db_connection(db_name)
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS forms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT NOT NULL,
                    salary INTEGER,
                    housing TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    pet_name TEXT NOT NULL
                )
            ''')

            # Insert sample data
            sample_forms = [
                (1, 'John Doe', 5000, 'Own a house', 'johndoe@example.com', 'Bella'),
                (3, 'Alice Johnson', 3900, 'Rent a apartment.', '999-888-4507', 'Max'),
            ]
            cursor.executemany(
                'INSERT INTO forms (user_id, name, salary, housing, contact, pet_name) VALUES (?, ?, ?, ?, ?, ?)',
                sample_forms)
            conn.commit()
        except sqlite3.Error as e: # pylint: disable=W0621
            print(f"Error initializing user database: {e}")
        finally:
            conn.close()
    else: 
            print("Failed to initialize forms database due to connection error.")

def initialize_all():
    """
    Calls all individual initialization functions to set up the databases.
    """
    init_user_db()
    init_pets_db()
    init_form_db()
    print("All databases initialized.")

# Running this file will initialize the databases.
#if __name__ == '__main__':
#    initialize_all()
