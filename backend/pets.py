"""This is pets.py that has examples of pets and methods associted with a pet's bio info"""
# pets.py
import sqlite3

# Connect to the pets.db SQLite database
connection = sqlite3.connect('pets.db')
cursor = connection.cursor()

def get_db_connection(name):
    """Establish a connection to the specified SQLite database."""
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row  # Optional, allows dictionary-like access to rows
    return conn

# Fetch pets from the database
def fetch_pets_from_db():
    """Fetches all pets from the database."""
    conn = get_db_connection('pets.db')
    cursor = conn.cursor()  # pylint: disable=W0621
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()  # pylint: disable=W0621
    conn.close()
    return pets

# Initialize pets
pets = fetch_pets_from_db()

def get_all_pets():
    """Returns a list of all pets directly from the database."""
    conn = get_db_connection('pets.db')
    cursor = conn.cursor()  # pylint: disable=W0621
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()  # pylint: disable=W0621
    conn.close()
    return [dict(pet) for pet in pets]


def get_pet_by_id(pet_id):
    """Fetches a single pet by ID directly from the database."""
    conn = get_db_connection('pets.db')
    cursor = conn.cursor()  # pylint: disable=W0621
    cursor.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
    pet = cursor.fetchone()
    conn.close()
    return dict(pet) if pet else None

# def create_pet(pet_data):
#     """Adds a new pet to the database."""
#     conn = get_db_connection('pets.db')
#     cursor = conn.cursor()  # pylint: disable=W0621
#
#     # Insert new pet into the database
#     cursor.execute(
#         "INSERT INTO pets (name, breed, age, description) VALUES (?, ?, ?, ?)",
#         (pet_data.get("name"), pet_data.get("breed", "Unknown"),
#           pet_data.get("age"), pet_data.get("description", "No description available"))
#     )
#     conn.commit()
#
#     # Get the ID of the newly inserted pet
#     new_pet_id = cursor.lastrowid
#     conn.close()
#
#     # Return the new pet with the assigned ID
#     return {
#         "id": new_pet_id,
#         "name": pet_data.get("name"),
#         "breed": pet_data.get("breed", "Unknown"),
#         "age": pet_data.get("age"),
#         "description": pet_data.get("description", "No description available")
#     }


# def update_pet(table, id, col, value):  # pylint: disable=W0622,C0103
#     """Updates a specific pet's information in the database."""
#     try:
#         connection = sqlite3.connect("pets.db")  # pylint: disable=W0621
#         cursor = connection.cursor()  # pylint: disable=W0621

#         # Use parameterized queries to avoid SQL injection
#         query = f"UPDATE {table} SET {col} = ? WHERE id = ?"
#         cursor.execute(query, (value, id))

#         # Check if any row was updated
#         if cursor.rowcount == 0:
#             return False

#         connection.commit()
#         return True
#     except sqlite3.Error as error:
#         print(f"Database error: {error}")
#         return False
#     finally:
#         connection.close()

# def delete_pet(pet_id):
#     """Deletes a pet by ID from the database."""
#     conn = get_db_connection('pets.db')
#     cursor = conn.cursor()  # pylint: disable=W0621

#     cursor.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
#     conn.commit()

#     if cursor.rowcount == 0:
#         conn.close()
#         return False

#     conn.close()
#     return True
