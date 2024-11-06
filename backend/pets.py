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
        "type": pet_data.get("type"),
        "age": pet_data.get("age")
    }
    pets.append(new_pet)
    return new_pet

def update_pet(pet_id, pet_data):
    """Updates an existing pet's information by ID."""
    pet = get_pet_by_id(pet_id)
    if pet:
        pet["name"] = pet_data.get("name", pet["name"])
        pet["type"] = pet_data.get("type", pet["type"])
        pet["age"] = pet_data.get("age", pet["age"])
        return pet
    return None

def delete_pet(pet_id):
    """Deletes a pet by ID without using the global keyword."""
    pet = next((p for p in pets if p["id"] == pet_id), None)
    if pet:
        # Reassign pets to a new list excluding the pet with the given ID
        pets[:] = [p for p in pets if p["id"] != pet_id]
        return True  # Indicates successful deletion
    return False  # Indicates pet was not found
