# users.py
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
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
