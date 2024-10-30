import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_list_pets():
    """This is a test for pet list"""
    response = requests.get(f"{BASE_URL}/pets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_pet():
    response = requests.get(f"{BASE_URL}/pets/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_add_pet():
    pet_data = {"name": "Rex", "type": "Dog", "age": 2}
    response = requests.post(f"{BASE_URL}/pets", json=pet_data)
    assert response.status_code == 201
    assert response.json()["name"] == pet_data["name"]

def test_update_pet():
    updated_data = {"name": "Rexy", "type": "Dog", "age": 3}
    response = requests.put(f"{BASE_URL}/pets/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]

def test_delete_pet():
    response = requests.delete(f"{BASE_URL}/pets/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Pet deleted successfully"

#user tests
def test_register_user():
    user_data = {"name": "David", "email": "david@example.com"}
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["name"] == user_data["name"]
    assert response.json()["email"] == user_data["email"]

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Alice"

def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/999")
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"

def test_get_user_adoption_progress():
    response = requests.get(f"{BASE_URL}/users/1")  # Get user info
    assert response.status_code == 200
    assert "adoption_progress" in response.json()

#manager tests
def test_manager_get_pet_info():
    response = requests.get(f"{BASE_URL}/pets/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_manager_add_pet():
    pet_data = {"name": "Coco", "type": "Dog", "age": 2}
    response = requests.post(f"{BASE_URL}/pets", json=pet_data)
    assert response.status_code == 201
    assert response.json()["name"] == pet_data["name"]

def test_manager_delete_pet():
    response = requests.delete(f"{BASE_URL}/pets/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Pet deleted successfully"

def test_manager_get_user_adoption_progress():
    response = requests.get(f"{BASE_URL}/users/3/adoption-progress")  # Adjust endpoint as necessary
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_manager_get_user_info():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Alice"

def test_manager_get_nonexistent_user_adoption_progress():
    response = requests.get(f"{BASE_URL}/users/999/adoption-progress")  # Assuming this user ID does not exist
    assert response.status_code == 404
    assert response.json()["error"] == "User with ID 999 not found or no adoption progress available"