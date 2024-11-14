import React, { useState } from 'react';

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  description: string;
  image: string;  // Added image property
}

const Pets: React.FC = () => {
  const [pets] = useState<Pet[]>([
    { id: 1, name: 'Bella', breed: 'Labrador', age: 3, description: 'Friendly and energetic.', image: '/images/Labrador.png' },
    { id: 2, name: 'Max', breed: 'Golden Retriever', age: 5, description: 'Loyal and calm.', image: '/images/Golden Retriever.png' },
    { id: 3, name: 'Lucy', breed: 'Bulldog', age: 2, description: 'Playful and loving.', image: '/images/Bulldog.png' },
  ]);

  const [selectedPet, setSelectedPet] = useState<Pet | null>(null);

  const handleViewDetails = (pet: Pet) => {
    setSelectedPet(pet);
  };

  return (
    <div style={{ padding: '2rem', textAlign: 'center'}}>
      <h1>Pets Page</h1>
      <p>This is where you can browse all available pets for adoption.</p>

      <div style={{ marginTop: '2rem', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        {pets.map((pet) => (
          <div key={pet.id} style={{ marginBottom: '1rem', textAlign: 'center', display: 'flex', alignItems: 'center' }}>
            <img src={pet.image} alt={`${pet.name}`} style={{ width: '70px', height: '70px', borderRadius: '1%', marginRight: '2rem' }} />
            <span>{pet.name}</span>
            <button onClick={() => handleViewDetails(pet)} style={{ marginLeft: '1rem'}}>
              View Details
            </button>
          </div>
        ))}
      </div>

      {selectedPet && (
        <div style={{ marginTop: '2rem'}}>
          <h2>{selectedPet.name}</h2>
          <p>Breed: {selectedPet.breed}</p>
          <p>Age: {selectedPet.age}</p>
          <p>Description: {selectedPet.description}</p>
          <button onClick={() => setSelectedPet(null)} >
            Close
          </button>
        </div>
      )}
    </div>
  );
};

export default Pets;
