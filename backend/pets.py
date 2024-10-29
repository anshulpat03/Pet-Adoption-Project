# pets.py
pets = [
    {"id": 1, "name": "Buddy", "type": "Dog", "age": 3},
    {"id": 2, "name": "Mittens", "type": "Cat", "age": 5}
]

def get_all_pets():
    """Returns a list of all pets."""
    return pets

def get_pet_by_id(pet_id):
    """Fetches a single pet by ID."""
    for pet in pets:
        if pet["id"] == pet_id:
            return pet
    return None

def create_pet(pet_data):
    """Adds a new pet to the collection."""
    new_id = max(pet["id"] for pet in pets) + 1 if pets else 1
    new_pet = {
        "id": new_id,
        "name": pet_data.get("name"),
        "type": pet_data.get("type"),
        "age": pet_data.get("age")
    }
    pets.append(new_pet)
    return new_pet

def update_pet(pet_id, pet_data):
    """Updates an existing pet's information by ID."""
    pet = get_pet_by_id(pet_id)
    if pet:
        pet["name"] = pet_data.get("name", pet["name"])
        pet["type"] = pet_data.get("type", pet["type"])
        pet["age"] = pet_data.get("age", pet["age"])
        return pet
    return None

def delete_pet(pet_id):
    """Removes a pet by ID."""
    global pets
    pet = get_pet_by_id(pet_id)
    if pet:
        pets = [p for p in pets if p["id"] != pet_id]
        return True
    return False
