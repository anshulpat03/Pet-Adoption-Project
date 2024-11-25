import React from "react";
import "./EditPetForm.css";

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  description: string;
  image: string;
}

interface EditPetFormProps {
  pet: Pet;
  onClose: () => void;
  onSubmit: (updatedPet: Pet) => void;
}

const EditPetForm: React.FC<EditPetFormProps> = ({ pet, onClose, onSubmit }) => {
  const handleEditPet = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const updatedPet = {
      id: pet.id,
      name: formData.get("name")?.toString() || pet.name,
      breed: formData.get("breed")?.toString() || pet.breed,
      age: parseInt(formData.get("age")?.toString() || `${pet.age}`, 10),
      description: formData.get("description")?.toString() || pet.description,
      image: formData.get("image")?.toString() || pet.image,
    };

    fetch(`http://localhost:5000/pets/${pet.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updatedPet),
    })
      .then((response) => {
        if (response.ok) {
          onSubmit(updatedPet);
          onClose();
        } else {
          console.error("Failed to update pet");
        }
      })
      .catch((error) => console.error("Error updating pet:", error));
  };

  return (
    <form onSubmit={handleEditPet} className="edit-pet-form">
      <h2>Edit Pet</h2>
      <div className="form-group">
        <label>Name:</label>
        <input type="text" name="name" defaultValue={pet.name} required />
      </div>
      <div className="form-group">
        <label>Breed:</label>
        <input type="text" name="breed" defaultValue={pet.breed} required />
      </div>
      <div className="form-group">
        <label>Age:</label>
        <input type="number" name="age" defaultValue={pet.age} required />
      </div>
      <div className="form-group">
        <label>Description:</label>
        <textarea name="description" defaultValue={pet.description} required />
      </div>
      <div className="form-group">
        <label>Image URL:</label>
        <input type="text" name="image" defaultValue={pet.image} required />
      </div>
      <div className="form-buttons">
        <button type="submit" className="btn submit-btn">
          Save Changes
        </button>
        <button type="button" className="btn cancel-btn" onClick={onClose}>
          Cancel
        </button>
      </div>
    </form>
  );
};

export default EditPetForm;
