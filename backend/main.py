
"""
This module provides a Flask web server with routes for managing pets and users.
"""
from database import initialize_all
from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from pets import get_all_pets, get_pet_by_id, create_pet, update_pet, delete_pet
from user import get_user_by_id, get_adoption_status
from user import fetch_users_from_db, login_user, register_user, add_form
from manager import (
    manager_get_pet_info,
    manager_add_pet,
    manager_delete_pet,
    manager_get_user_adoption_progress
)

# Initialize Flask app and enable CORS
def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: The initialized Flask application instance.
    """
    app = Flask(__name__) # pylint: disable=all
    initialize_all()  # Ensure the database is initialized
    return app

app = create_app()
CORS(app)

# Swagger setup for API documentation
swagger_spec = {
    'definitions': {
        'Pet': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'name': {'type': 'string'},
                'breed': {'type': 'string'},
                'age': {'type': 'integer'}
            }
        },
        'User': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'name': {'type': 'string'},
                'email': {'type': 'string'}
            }
        }
    }
}
swagger = Swagger(app, template=swagger_spec)

# Initialize Database
def initialize_database():
    """Initialize database connections for all categories."""
    initialize_all()

# Welcome route
@app.route('/', methods=['GET'])
def welcome():
    """Find your new best friend!"""
    return jsonify({"message": "Welcome to the pet adoption website!"}), 200

# Pet Routes
@app.route('/pets', methods=['GET'])
def list_pets():
    """Fetch all pets."""
    pets = get_all_pets()
    return jsonify(pets)

@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """Fetch a pet by its ID."""
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({"error": "Pet not found"}), 404

@app.route('/pets', methods=['POST'])
def add_pet():
    """Add a new pet."""
    data = request.get_json()
    new_pet = create_pet(data)
    return jsonify(new_pet), 201

@app.route('/pets/<int:pet_id>', methods=['PUT'])
def edit_pet(pet_id):
    """Update a pet's information."""
    data = request.get_json()
    updated_pet = False
    for col, value in data.items():
        if update_pet("pets", pet_id, col, value):  # Pass table name ("pets")
            updated_pet = True

    if updated_pet:
        # Retrieve updated pet from database (this is optional, but can be useful for confirmation)
        updated_pet_data = get_pet_by_id(pet_id)
        return jsonify(updated_pet_data), 200
    return jsonify({"error": "Pet not found"}), 404

@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def remove_pet(pet_id):
    """Delete a pet by ID."""
    print(f"Attempting to delete pet with ID: {pet_id}")
    success = delete_pet(pet_id)
    if success:
        return jsonify({"message": "Pet deleted successfully"}), 200
    return jsonify({"error": "Pet not found"}), 404

# User Routes
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Fetch a user by ID."""
    user = get_user_by_id(int(user_id))
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['GET'])
def get_all_users():
    """Fetch all users and their adoption progress."""
    users = fetch_users_from_db()
    if users:
        return jsonify([dict(user) for user in users]), 200
    return jsonify({"error": "No users found"}), 404

@app.route('/users/<int:user_id>/status', methods=['GET'])
def fetch_adoption_status(user_id):
    """Fetch the adoption status of a user."""
    status = get_adoption_status(user_id)
    if status:
        return jsonify({"user_id": user_id, "adoption_status": status}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/login', methods=['POST'])
def login():
    """Login a user by validating username and password."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = login_user(username, password)

    if user:
        return jsonify({"message": "Login successful", "user_id": user["id"]}), 200
    return jsonify({"error": "Invalid username or password"}), 401


#@app.route('/users/<int:user_id>/status', methods=['PUT'])
#def modify_adoption_status(user_id):
    """Update the adoption status of a user.""" # pylint: disable=all
    data = request.get_json()
    new_status = data.get("adoption_status")
    if new_status not in ["pending", "accepted", "denied"]:
        return jsonify({"error": "Invalid status"}), 400
    updated = update_adoption_status(user_id, new_status) # pylint: disable=all
    return jsonify(updated), 200

@app.route('/users', methods=['POST'])
def register_new_user():
    """Register a new user."""
    data = request.get_json()
    new_user = register_user(data)
    return jsonify(new_user), 201
  
@app.route('/form', methods=['POST'])
def apply_to_adopt():
    """Fill out application form to adopt pet"""
    data = request.get_json()
    new_application = add_form(data)
    if new_application:
        return jsonify({"message": "We received your form. Thank you for applying!"}), 200
    return jsonify({"error": "something went wrong"}), 404

# Manager Routes
@app.route('/manager/pet/<int:pet_id>', methods=['GET'])
def manager_pet_info(pet_id):
    """Manager access: Get detailed info about a pet."""
    pet_info = manager_get_pet_info(pet_id)
    if pet_info:
        return jsonify(pet_info), 200
    return jsonify({"error": "Pet not found"}), 404

@app.route('/manager/pet', methods=['POST'])
def manager_add_new_pet():
    """Manager access: Add a new pet to the system."""
    data = request.get_json()
    pet = manager_add_pet(data)
    return jsonify(pet), 201

@app.route('/manager/pet/<int:pet_id>', methods=['DELETE'])
def manager_remove_pet(pet_id):
    """Manager access: Delete a pet by ID."""
    success = manager_delete_pet(pet_id)
    if success:
        return jsonify({"message": "Pet deleted successfully"}), 200
    return jsonify({"error": "Pet not found"}), 404

@app.route('/manager/user/<int:user_id>/adoption-progress', methods=['GET'])
def manager_view_user_adoption_progress(user_id):
    """Manager access: View a user’s adoption progress."""
    progress = manager_get_user_adoption_progress(user_id)
    if progress:
        return jsonify(progress), 200
    return jsonify({"error": "User or progress not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
