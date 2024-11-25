import React, { useEffect, useState } from "react";
import EditPetForm from "../components/EditPetForm";
import "./AdminPetList.css";

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  description: string;
  image: string;
}

const AdminPetList: React.FC = () => {
  const [pets, setPets] = useState<Pet[]>([]);
  const [editingPet, setEditingPet] = useState<Pet | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/pets")
      .then((response) => response.json())
      .then((data) => setPets(data))
      .catch((error) => console.error("Error fetching pets:", error));
  }, []);

  

  const handleRemovePet = (id: number) => {
    // Confirm before deleting
    if (!window.confirm("Are you sure you want to remove this pet?")) {
      return;
    }

    // Make a DELETE request to the backend
    fetch(`http://localhost:5000/pets/${id}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          // Update state to reflect the removed pet
          setPets((prevPets) => prevPets.filter((pet) => pet.id !== id));
        } else {
          console.error("Failed to delete pet");
        }
      })
      .catch((error) => console.error("Error deleting pet:", error));
  };
  const handleEditPet = (updatedPet: Pet) => {
    setPets((prevPets) =>
      prevPets.map((pet) => (pet.id === updatedPet.id ? updatedPet : pet))
    );
  };

  return (
    <div className="admin-pet-list">
      {pets.map((pet) => (
        <div key={pet.id} className="pet-card">
          <img src={pet.image} alt={pet.name} className="pet-image" />
          <h3>{pet.name}</h3>
          <p>
            <strong>Breed:</strong> {pet.breed}
          </p>
          <p>
            <strong>Age:</strong> {pet.age}
          </p>
          <p>
            <strong>Description:</strong> {pet.description}
          </p>
          <button
              className="btn remove-pet-btn"
              onClick={() => handleRemovePet(pet.id)}
            >
              Remove Pet
          </button>

          <button
              className="btn edit-pet-btn"
              onClick={() => setEditingPet(pet)}
            >
              Edit Pet
          </button>

        </div>
      ))}
      {editingPet && (
        <div className="popup-overlay">
          <div className="popup-container">
            <EditPetForm
              pet={editingPet}
              onClose={() => setEditingPet(null)}
              onSubmit={handleEditPet}
            />
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminPetList;
