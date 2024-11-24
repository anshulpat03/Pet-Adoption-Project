import React, { useEffect, useState } from "react";
import Pet from "../components/Pet.tsx";

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  description: string;
  image: string;
}

const Pets: React.FC = () => {
  const [pets, setPets] = useState<Pet[]>([]);
  const [selectedPet, setSelectedPet] = useState<Pet | null>(null);
  const [searchTerm, setSearchTerm] = useState<string>("");

  useEffect(() => {
    fetch("http://localhost:5000/pets")
      .then((response) => response.json())
      .then((data) => setPets(data))
      .catch((error) => console.error("Error fetching pets:", error));
  }, []);

  const handleViewDetails = (pet: Pet) => {
    setSelectedPet(pet);
  };

  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const filteredPets = pets.filter(
    (pet) =>
      pet.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      pet.breed.toLowerCase().includes(searchTerm.toLowerCase()) ||
      pet.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ padding: "2rem", textAlign: "center" }}>
      <h1>Pets Page</h1>
      <p>This is where you can browse all available pets for adoption.</p>

      <input
        type="text"
        placeholder="Search by name, breed, or description..."
        value={searchTerm}
        onChange={handleSearch}
        style={{
          padding: "0.5rem",
          width: "100%",
          maxWidth: "400px",
          marginBottom: "1rem",
          borderRadius: "5px",
          border: "1px solid #ccc",
        }}
      />

      <div style={{ display: "flex", alignItems: "flex-start", gap: "2rem" }}>
        <div style={{ flex: 1 }}>
          {filteredPets.length > 0 ? (
            filteredPets.map((pet) => (
              <Pet key={pet.id} pet={pet} onViewDetails={handleViewDetails} />
            ))
          ) : (
            <p>No pets found at this moment :(</p>
          )}
        </div>

        <div style={{ flex: "0 0 300px", padding: "1rem", borderRadius: "8px" }}>
          {selectedPet ? (
            <>
              <h2>{selectedPet.name}</h2>
              <p>
                <strong>Breed:</strong> {selectedPet.breed}
              </p>
              <p>
                <strong>Age:</strong> {selectedPet.age}
              </p>
              <p>
                <strong>Description:</strong> {selectedPet.description}
              </p>
              <button onClick={() => setSelectedPet(null)}>Close</button>
            </>
          ) : (
            <p>Select a pet to see details here</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Pets;
