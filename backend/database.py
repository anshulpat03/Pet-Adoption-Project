import sqlite3, os

def get_db_connection(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row  # Optional, allows dictionary-like access to rows
    return conn

def init_pet_db():
    name = 'pets.db'
    conn = get_db_connection(name)
    cursor = conn.cursor()
    
    # Example table creation based on a pet adoption schema
    cursor.execute('''CREATE TABLE IF NOT EXISTS pets (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        breed TEXT,
                        age INTEGER,
                        description TEXT)''')
    
    # Insert any initial data if necessary
    cursor.execute('SELECT COUNT(*) FROM pets WHERE name = "Buddy"')
    count = cursor.fetchone()[0]
    
    # Insert the pet if it does not already exist
    if count == 0:
        cursor.execute('''INSERT INTO pets (name, breed, age, description)
                          VALUES (?, ?, ?, ?)''', 
                       ('Buddy', 'Golden Retriever', 3, 'Friendly and active'))
    
    conn.commit()
    conn.close()

def init_user_db():
    if os.path.exists("user.db"):
        os.remove("user.db")
    name = 'users.db'
    conn = get_db_connection(name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE)''')
    cursor.execute('''INSERT INTO users (username, email)
                    VALUES(?,?)''', 
                    ('John Doe', 'johndoe@example.com'))
    
    conn.commit()
    conn.close()
    
def init_db():
    init_pet_db()
    #init_user_db()