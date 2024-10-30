# users.py
users = [
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

def get_user_by_id(user_id):
    """Fetches a user by their ID."""
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def register_user(user_data):
    """Registers a new user."""
    new_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": user_data.get("name"),
        "email": user_data.get("email")
    }
    users.append(new_user)
    return new_user

def get_user_adoption_progress(user_id):
    """Retrieve a user's adoption progress."""
    user = get_user_by_id(user_id)
    if user:
        return user.get("adoption_progress", [])
    return {"error": "User not found"}

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