"""This is pets.py that has examples of pets and methods associted with a pet's bio info"""
# pets.py
import sqlite3

# Connect to the pets.db SQLite database
connection = sqlite3.connect('pets.db')
cursor = connection.cursor()

def get_db_connection(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row  # Optional, allows dictionary-like access to rows
    return conn

# Fetch pets from the database
def fetch_pets_from_db():
    conn = get_db_connection('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()
    conn.close()
    return pets

# Initialize pets
pets = fetch_pets_from_db()

def get_all_pets():
    """Returns a list of all pets."""
    return [dict(pet) for pet in pets]

def get_pet_by_id(pet_id):
    """Fetches a single pet by ID."""
    for pet in pets:
        if pet["id"] == pet_id:
            return dict(pet)
    return None

def create_pet(pet_data):
    """Adds a new pet to the collection."""
    new_id = max(pet["id"] for pet in pets) + 1 if pets else 1
    new_pet = {
        "id": new_id,
        "name": pet_data.get("name"),
        "breed": pet_data.get("breed"),
        "age": pet_data.get("age"),
        "description": pet_data.get("description")
    }
    pets.append(new_pet)
    return new_pet

def update_pet(table, id, col, value):
    try:
        connection = sqlite3.connect("pets.db")
        cursor = connection.cursor()
        
        # Use parameterized queries to avoid SQL injection
        query = f"UPDATE {table} SET {col} = ? WHERE id = ?"
        cursor.execute(query, (value, id))
        
        # Check if any row was updated
        if cursor.rowcount == 0:
            return False
        
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()
        
def delete_pet(pet_id):
    """Deletes a pet by ID without using the global keyword."""
    pet = next((p for p in pets if p["id"] == pet_id), None)
    if pet:
        # Reassign pets to a new list excluding the pet with the given ID
        pets[:] = [p for p in pets if p["id"] != pet_id]
        return True  # Indicates successful deletion
    return False  # Indicates pet was not found
