import React, { useEffect, useState } from "react";
import "./AdminPetList.css";

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  description: string;
  image: string;
  applicants: { id: number; name: string; status: string }[];
}

const AdminPetList: React.FC = () => {
  const [pets, setPets] = useState<Pet[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/pets")
      .then((response) => response.json())
      .then((data) => setPets(data))
      .catch((error) => console.error("Error fetching pets:", error));
  }, []);

  
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
        </div>
      ))}
    </div>
  );
};

export default AdminPetList;
