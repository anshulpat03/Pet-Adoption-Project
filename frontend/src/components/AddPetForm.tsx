import React from "react";
import "./AddPetForm.css";

interface AddPetFormProps {
  onClose: () => void;
}

const AddPetForm: React.FC<AddPetFormProps> = ({ onClose }) => {
  const handleAddPet = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const newPet = {
      name: formData.get("name"),
      breed: formData.get("breed"),
      age: parseInt(formData.get("age") as string, 10),
      description: formData.get("description"),
      image: formData.get("image"),
    };

    fetch("http://localhost:5000/pets", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newPet),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Pet added:", data);
        onClose();
      })
      .catch((error) => console.error("Error adding pet:", error));
  };

  return (
    <form onSubmit={handleAddPet} className="add-pet-form">
      <h2>Add a New Pet</h2>
      <div className="form-group">
        <label>Name:</label>
        <input type="text" name="name" required />
      </div>
      <div className="form-group">
        <label>Breed:</label>
        <input type="text" name="breed" required />
      </div>
      <div className="form-group">
        <label>Age:</label>
        <input type="number" name="age" required />
      </div>
      <div className="form-group">
        <label>Description:</label>
        <textarea name="description" required />
      </div>
      <div className="form-group">
        <label>Image URL:</label>
        <input type="text" name="image" required />
      </div>
      <div className="form-buttons">
        <button type="submit" className="btn submit-btn">
          Submit
        </button>
        <button type="button" className="btn cancel-btn" onClick={onClose}>
          Cancel
        </button>
      </div>
    </form>
  );
};

export default AddPetForm;