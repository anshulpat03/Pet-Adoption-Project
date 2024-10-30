from flask import Flask, jsonify, request
from flask_cors import CORS
from pets import get_all_pets, get_pet_by_id, create_pet, update_pet, delete_pet
from user import get_user_by_id, register_user

app = Flask(__name__)
CORS(app)

# Pets Routes
@app.route('/pets', methods=['GET'])
def list_pets():
    """Get a list of all pets"""
    return jsonify(get_all_pets()), 200

@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """Get details of a specific pet by pet ID"""
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet), 200
    else:
        return jsonify({'error': 'Pet not found'}), 404

@app.route('/pets', methods=['POST'])
def add_pet():
    """Add a new pet to the system"""
    pet_data = request.json
    new_pet = create_pet(pet_data)
    return jsonify(new_pet), 201

@app.route('/pets/<int:pet_id>', methods=['PUT'])
def edit_pet(pet_id):
    """Update pet details by pet ID"""
    pet_data = request.json
    updated_pet = update_pet(pet_id, pet_data)
    if updated_pet:
        return jsonify(updated_pet), 200
    else:
        return jsonify({'error': 'Pet not found'}), 404

@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def remove_pet(pet_id):
    """Delete a pet by pet ID"""
    success = delete_pet(pet_id)
    if success:
        return jsonify({'message': 'Pet deleted successfully'}), 200
    else:
        return jsonify({'error': 'Pet not found'}), 404

# User Routes
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user information by user ID"""
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    user_data = request.json
    new_user = register_user(user_data)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
