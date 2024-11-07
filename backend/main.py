
"""
This module provides a Flask web server with routes for managing pets and users
"""
from database import init_db
from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from pets import get_all_pets, get_pet_by_id, create_pet, update_pet, delete_pet, fetch_pets_from_db
from user import get_user_by_id, register_user
init_db()



app = Flask(__name__)
CORS(app)

swagger_spec = {
    'definitions': {
        'Pet': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer'
                },
                'name': {
                    'type': 'string'
                },
                'breed': {
                    'type': 'string'
                },
                'age': {
                    'type': 'integer'
                },
                'description': {
                    'type': 'string'
                }
            }
        }
    }
}


swagger = Swagger(app, template=swagger_spec)


# Pets Routes
@app.route('/')
def home():
    return "<p>Hello<p>"

@app.route('/pets', methods=['GET'])
def list_pets():
    """Get a list of all pets
    ---
    responses:
      200:
        description: A list of pets
        schema:
          type: array
          items:
            $ref: '#/definitions/Pet'
    """
    return jsonify(get_all_pets()), 200

@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """Get details of a specific pet by pet ID
    ---
    parameters:
      - name: pet_id
        in: path
        type: integer
        required: true
        description: The ID of the pet
    responses:
      200:
        description: Pet found
        schema:
          $ref: '#/definitions/Pet'
      404:
        description: Pet not found
    """
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({'error': 'Pet not found'}), 404

@app.route('/pets', methods=['POST'])
def add_pet():
    """
    Add a new pet
    ---
    parameters:
      - name: body
        in: body
        required: true
        description: Pet object that needs to be added
        schema:
          $ref: '#/definitions/Pet'
    responses:
      201:
        description: Pet created successfully
        schema:
          $ref: '#/definitions/Pet'
      400:
        description: Invalid input
    """
    pet_data = request.json
    new_pet = create_pet(pet_data)
    return jsonify(new_pet), 201

@app.route('/pets/<int:pet_id>', methods=['PUT'])
def edit_pet(pet_id):
    """
    Update a pet's information
    ---
    parameters:
      - name: pet_id
        in: path
        type: integer
        required: true
        description: The ID of the pet to update
      - name: body
        in: body
        required: true
        description: The new data for the pet
        schema:
          $ref: '#/definitions/Pet'
    responses:
      200:
        description: Pet updated successfully
        schema:
          $ref: '#/definitions/Pet'
      400:
        description: Invalid input
      404:
        description: Pet not found
    """
    pet_data = request.json
    for col, value in pet_data.items():
        update_result = update_pet("pets", pet_id, col, value)
        if not update_result:
            return jsonify({'error': f'Failed to update {col}'}), 400

    global pets
    pets = fetch_pets_from_db()

    updated_pet = get_pet_by_id(pet_id)
    if updated_pet:
        return jsonify(updated_pet), 200
    return jsonify({'error': 'Pet not found'}), 404

@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def remove_pet(pet_id):
    """
    Delete a pet by pet ID
    ---
    parameters:
      - name: pet_id
        in: path
        type: integer
        required: true
        description: The ID of the pet to delete
    responses:
      200:
        description: Pet deleted successfully
      404:
        description: Pet not found
    """
    success = delete_pet(pet_id)
    if success:
        return jsonify({'message': 'Pet deleted successfully'}), 200
    return jsonify({'error': 'Pet not found'}), 404

# User Routes
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user information by user ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
    responses:
      200:
        description: User found
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    """
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/register', methods=['POST'])
def register():
    """Register a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        description: User object that needs to be registered
        schema:
          $ref: '#/definitions/User'
    responses:
      201:
        description: User registered successfully
        schema:
          $ref: '#/definitions/User'
      400:
        description: Invalid input
    """
    user_data = request.json
    new_user = register_user(user_data)
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)
