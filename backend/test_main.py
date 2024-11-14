"""
Test suite for the Pet Adoption Organization API.
Contains tests for endpoints related to pets, users, and managers.
"""
import pytest
from main import app  # Import your Flask app

@pytest.fixture
def test_client():
    """Fixture to set up Flask test client."""
    with app.test_client() as test_client: # pylint: disable=W0621
        yield test_client

def test_list_pets(test_client): # pylint: disable=W0621
    """Test listing all pets."""
    response = test_client.get('/pets')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check that the response is a list

def test_get_pet(test_client): # pylint: disable=W0621
    """Test retrieving a pet by ID."""
    # Ensure pet with ID 1 exists, create if not
    response = test_client.get('/pets/1')
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert 'name' in response.json
        assert 'breed' in response.json
    elif response.status_code == 404:
        # Check if pet not found error is returned
        assert response.json['error'] == "Pet not found"

# def test_add_pet(test_client): # pylint: disable=W0621
#     """Test adding a new pet."""
#     new_pet = {"name": "Max",
#                 "breed": "Labrador",
#                   "age": 2,
#                       "description": "Friendly and playful"}
#     response = test_client.post('/pets', json=new_pet)
#     assert response.status_code == 201  # Created
#     assert response.json['name'] == new_pet['name']
#     assert response.json['breed'] == new_pet['breed']

# def test_update_pet(test_client): # pylint: disable=W0621
#     """Test updating a pet's information."""
#     new_pet = {"name": "Max", "breed": "Labrador", "age": 2, "description": "Friendly"}
#     create_response = test_client.post('/pets', json=new_pet)
#     pet_id = create_response.json['id']

#     update_data = {"name": "Fluffy"}
#     response = test_client.put(f'/pets/{pet_id}', json=update_data)  # Assuming pet with ID 1 exists
#     assert response.status_code in [200, 404]
#     if response.status_code == 200:
#         assert response.json['name'] == "Fluffy"
#     elif response.status_code == 404:
#         # Verify the error message returned if pet not found
#         assert response.json['error'] == "Pet not found"

# def test_delete_pet(test_client): # pylint: disable=W0621
#     """Test deleting a pet by ID."""
#     # Create a pet first
#     new_pet = {"name": "Max", "breed": "Labrador", "age": 2, "description": "Friendly"}
#     create_response = test_client.post('/pets', json=new_pet)
#     pet_id = create_response.json['id']  # Get the ID of the newly created pet

#     # Now delete the pet
#     response = test_client.delete(f'/pets/{pet_id}')
#     assert response.status_code in [200, 404]
#     if response.status_code == 200:
#         assert response.json['message'] == "Pet deleted successfully"

# def test_get_user(test_client): # pylint: disable=W0621
#     """Test retrieving a user by ID."""
#     # Assuming user with ID 1 exists
#     response = test_client.get('/users/1')
#     assert response.status_code in [200, 404]
#     if response.status_code == 200:
#         assert 'username' in response.json
#         assert 'email' in response.json

# def test_register_user(test_client): # pylint: disable=W0621
#     """Test registering a new user."""
#     # Ensures a unique email
#     new_user = {
#         "name": "Dave",
#         "email": "dave102@example.com"
#     }
#     response = test_client.post('/register', json=new_user)
#     assert response.status_code == 201  # Created
#     assert 'id' in response.json
#     assert response.json['email'] == new_user['email']
#     assert response.json['name'] == new_user['name']
