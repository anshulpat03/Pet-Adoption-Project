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
