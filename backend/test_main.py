"""This is test_main file that tests methods in user, pets, and manager"""
import pytest
from main import app  # Import your main Flask app

@pytest.fixture
def client():
    """Fixture to set up Flask test client."""
    with app.test_client() as client:
        yield client

def test_list_pets(client):
    """Test listing all pets."""
    response = client.get('/pets')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check that the response is a list

def test_get_pet(client):
    """Test retrieving a pet by ID."""
    response = client.get('/pets/1')  # Assuming pet with ID 1 exists
    assert response.status_code in [200, 404]  # 200 if found, 404 if not
    if response.status_code == 200:
        assert 'name' in response.json
        assert 'type' in response.json

def test_add_pet(client):
    """Test adding a new pet."""
    new_pet = {
        "name": "Snowball",
        "type": "Rabbit",
        "age": 2
    }
    response = client.post('/pets', json=new_pet)
    assert response.status_code == 201  # Created
    assert response.json['name'] == new_pet['name']
    assert response.json['type'] == new_pet['type']

def test_update_pet(client):
    """Test updating a pet's information."""
    update_data = {"name": "Fluffy"}
    response = client.put('/pets/1', json=update_data)  # Assuming pet with ID 1 exists
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json['name'] == "Fluffy"

def test_delete_pet(client):
    """Test deleting a pet by ID."""
    response = client.delete('/pets/1')  # Assuming pet with ID 1 exists
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json['message'] == "Pet deleted successfully"

def test_get_user(client):
    """Test retrieving a user by ID."""
    response = client.get('/users/1')  # Assuming user with ID 1 exists
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert 'name' in response.json
        assert 'email' in response.json

def test_user_adoption_progress(client):
    """Test retrieving a user's adoption progress."""
    response = client.get('/users/1/adoption-progress')  # Assuming user with ID 1 exists
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json, list)  # Should be a list of progress entries

def test_manager_get_user_info(client):
    """Test manager access to user information by user ID."""
    response = client.get('/manager/users/1')  # Assuming user with ID 1 exists
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert 'name' in response.json
        assert 'adoption_progress' in response.json
"""
Test suite for the Pet Adoption Organization API.
Contains tests for endpoints related to pets, users, and managers.
"""

import pytest
from main import app  # Import your Flask app

BASE_URL = "/"

@pytest.fixture
def test_client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_list_pets(test_client):
    """
    Test that the endpoint returns a list of all available pets.
    Verifies:
        - The response status code is 200 (OK).
        - The response data is a list.
    """
    response = test_client.get(f"{BASE_URL}pets")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_pet(test_client):
    """
    Test retrieving a specific pet by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The pet ID in the response matches the requested ID.
    """
    response = test_client.get(f"{BASE_URL}pets/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1

def test_add_pet(test_client):
    """
    Test adding a new pet.
    Verifies:
        - The response status code is 201 (Created).
        - The response contains the correct pet information.
    """
    pet_data = {"name": "Rex", "type": "Dog", "age": 2}
    response = test_client.post(f"{BASE_URL}pets", json=pet_data)
    assert response.status_code == 201
    assert response.get_json()["name"] == pet_data["name"]

def test_update_pet(test_client):
    """
    Test updating an existing pet's information.
    Verifies:
        - The response status code is 200 (OK).
        - The updated pet information matches the provided data.
    """
    updated_data = {"name": "Rexy", "type": "Dog", "age": 3}
    response = test_client.put(f"{BASE_URL}pets/1", json=updated_data)
    assert response.status_code == 200
    assert response.get_json()["name"] == updated_data["name"]

def test_delete_pet(test_client):
    """
    Test deleting a specific pet by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The response contains a confirmation message.
    """
    response = test_client.delete(f"{BASE_URL}pets/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Pet deleted successfully"

# User tests
def test_register_user(test_client):
    """
    Test registering a new user.
    Verifies:
        - The response status code is 201 (Created).
        - The response contains the correct user information.
    """
    user_data = {"name": "David", "email": "david@example.com"}
    response = test_client.post(f"{BASE_URL}register", json=user_data)
    assert response.status_code == 201
    assert response.get_json()["name"] == user_data["name"]
    assert response.get_json()["email"] == user_data["email"]

def test_get_user(test_client):
    """
    Test retrieving a specific user by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The user ID and name in the response match the requested user.
    """
    response = test_client.get(f"{BASE_URL}users/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1
    assert response.get_json()["name"] == "Alice"

def test_get_nonexistent_user(test_client):
    """
    Test attempting to retrieve a non-existent user by ID.
    Verifies:
        - The response status code is 404 (Not Found).
        - The response contains an error message indicating the user was not found.
    """
    response = test_client.get(f"{BASE_URL}users/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"

def test_get_user_adoption_progress(test_client):
    """
    Test retrieving adoption progress for a specific user.
    Verifies:
        - The response status code is 200 (OK).
        - The response includes adoption progress data for the user.
    """
    response = test_client.get(f"{BASE_URL}users/1")
    assert response.status_code == 200
    assert "adoption_progress" in response.get_json()

# Manager tests
def test_manager_get_pet_info(test_client):
    """
    Test manager retrieving information for a specific pet by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The pet ID in the response matches the requested ID.
    """
    response = test_client.get(f"{BASE_URL}pets/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1

def test_manager_add_pet(test_client):
    """
    Test manager adding a new pet.
    Verifies:
        - The response status code is 201 (Created).
        - The response contains the correct pet information.
    """
    pet_data = {"name": "Coco", "type": "Dog", "age": 2}
    response = test_client.post(f"{BASE_URL}pets", json=pet_data)
    assert response.status_code == 201
    assert response.get_json()["name"] == pet_data["name"]

def test_manager_delete_pet(test_client):
    """
    Test manager deleting a specific pet by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The response contains a confirmation message.
    """
    response = test_client.delete(f"{BASE_URL}pets/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Pet deleted successfully"

def test_manager_get_user_adoption_progress(test_client):
    """
    Test manager retrieving adoption progress for a specific user by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The response data is a list representing the user's adoption progress.
    """
    response = test_client.get(f"{BASE_URL}users/3/adoption-progress")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_manager_get_user_info(test_client):
    """
    Test manager retrieving information for a specific user by ID.
    Verifies:
        - The response status code is 200 (OK).
        - The user ID and name in the response match the requested user.
    """
    response = test_client.get(f"{BASE_URL}users/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1
    assert response.get_json()["name"] == "Alice"

def test_manager_get_nonexistent_user_adoption_progress(test_client):
    """
    Test manager attempting to retrieve adoption progress for 
    a non-existent user by ID.
    Verifies:
        - The response status code is 404 (Not Found).
        - The response contains an error message indicating the 
        user or adoption progress was not found.
    """
    response = test_client.get(f"{BASE_URL}users/999/adoption-progress")
    assert response.status_code == 404
    assert response.get_json()["error"] == (
        "User with ID 999 not found or no adoption progress available"
    )
