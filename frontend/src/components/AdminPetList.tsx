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

  const handleChangeStatus = (petId: number, applicantId: number, status: string) => {
    fetch(`http://localhost:5000/pets/${petId}/applicants/${applicantId}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Status updated:", data);
        setPets((prevPets) =>
          prevPets.map((pet) =>
            pet.id === petId
              ? {
                  ...pet,
                  applicants: pet.applicants.map((applicant) =>
                    applicant.id === applicantId ? { ...applicant, status } : applicant
                  ),
                }
              : pet
          )
        );
      })
      .catch((error) => console.error("Error updating status:", error));
  };

  return (
    <div className="admin-pet-list">
      <h2>Manage Pets</h2>
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
