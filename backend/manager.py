"""This is manager.py file to access user and pet information."""
# manager.py - Stubs for manager-specific API calls
from pets import get_pet_by_id # create_pet, delete_pet
from user import get_user_by_id # get_user_adoption_progress

def manager_get_pet_info(pet_id):
    """Manager access to get detailed pet information."""
    # Reuse get_pet_by_id from pets module to simulate this functionality
    return get_pet_by_id(pet_id)

# def manager_add_pet(pet_data):
#     """Manager ability to add a new pet."""
#     # Reuse create_pet from pets module to simulate adding functionality
#     return create_pet(pet_data)

# def manager_delete_pet(pet_id):
#     """Manager ability to delete a pet."""
#     # Reuse delete_pet from pets module to simulate deleting functionality
#     return delete_pet(pet_id)

def manager_get_user_info(user_id):
    """Manager access to get user information by user ID."""
    user = get_user_by_id(user_id)
    if not user:
        return {"error": f"User with ID {user_id} not found"}
    return user

# def get_adoption_progress_db_connection():
#     """
#     Establish a connection to the adoption_progress database.
#     """
#     try:
#         conn = sqlite3.connect('adoption_progress.db')
#         conn.row_factory = sqlite3.Row  # Enables dictionary-like access to rows
#         return conn
#     except sqlite3.Error as e:
#         print(f"Error connecting to adoption_progress database: {e}")
#         return None

# def manager_get_user_adoption_progress(user_id):
#     """
#     Retrieve the adoption progress for a specified user from the adoption_progress database.
#     """
#     conn = get_adoption_progress_db_connection()
#     if conn is None:
#         return None

#     try:
#         cursor = conn.cursor()
#         query = '''
#             SELECT ap.id AS adoption_id, ap.status, p.name AS pet_name, p.breed, p.age
#             FROM adoption_progress ap
#             JOIN pets p ON ap.pet_id = p.id
#             WHERE ap.user_id = ?
#         '''
#         cursor.execute(query, (user_id,))
#         progress_data = cursor.fetchall()

#         # Transform the result into a list of dictionaries for easier JSON serialization
#         adoption_progress = [
#             {"adoption_id": row["adoption_id"],
#              "status": row["status"],
#              "pet_name": row["pet_name"],
#              "breed": row["breed"],
#              "age": row["age"]}
#             for row in progress_data
#         ]

#         return {"user_id": user_id, "adoption_progress": adoption_progress}
#     except sqlite3.Error as e:
#         print(f"Error retrieving adoption progress: {e}")
#         return None
#     finally:
#         conn.close()

# def update_user_adoption_progress(user_id, pet_id, status):
#     """Update or add adoption progress for a user."""
#     user = get_user_by_id(user_id)
#     if not user:
#         return {"error": "User not found"}

#     # Check if there's already an entry for this pet_id
#     for progress in user["adoption_progress"]:
#         if progress["pet_id"] == pet_id:
#             progress["status"] = status  # Update status
#             return progress

#     # If no entry for the pet_id exists, add a new one
#     new_progress = {"pet_id": pet_id, "status": status}
#     user["adoption_progress"].append(new_progress)
#     return new_progress
