"""This is manager.py file to access user and pet information."""
# manager.py - Stubs for manager-specific API calls

from pets import get_pet_by_id, create_pet, delete_pet
from user import get_user_by_id, get_user_adoption_progress

def manager_get_pet_info(pet_id):
    """Manager access to get detailed pet information."""
    # Reuse get_pet_by_id from pets module to simulate this functionality
    return get_pet_by_id(pet_id)

def manager_add_pet(pet_data):
    """Manager ability to add a new pet."""
    # Reuse create_pet from pets module to simulate adding functionality
    return create_pet(pet_data)

def manager_delete_pet(pet_id):
    """Manager ability to delete a pet."""
    # Reuse delete_pet from pets module to simulate deleting functionality
    return delete_pet(pet_id)

def manager_get_user_adoption_progress(user_id):
    """Manager access to view a user’s adoption progress."""
    # Call get_user_adoption_progress from users module
    progress = get_user_adoption_progress(user_id)
    if "error" in progress:
        return {"error": f"User with ID {user_id} not found or no adoption progress available"}
    return progress

def manager_get_user_info(user_id):
    """Manager access to get user information by user ID."""
    user = get_user_by_id(user_id)
    if not user:
        return {"error": f"User with ID {user_id} not found"}
    return user

def update_user_adoption_progress(user_id, pet_id, status):
    """Update or add adoption progress for a user."""
    user = get_user_by_id(user_id)
    if not user:
        return {"error": "User not found"}

    # Check if there's already an entry for this pet_id
    for progress in user["adoption_progress"]:
        if progress["pet_id"] == pet_id:
            progress["status"] = status  # Update status
            return progress

    # If no entry for the pet_id exists, add a new one
    new_progress = {"pet_id": pet_id, "status": status}
    user["adoption_progress"].append(new_progress)
    return new_progress

# Example of how the manager might use this function

# Manager retrieves the adoption progress for user with ID 3 (Charlie)
# print(manager_get_user_adoption_progress(3))

# Expected Output:
# [{'pet_id': 3, 'status': 'Denied'}]
