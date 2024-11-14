import React, { useState } from 'react';

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  description: string;
  image: string;
}

const Pets: React.FC = () => {
  const [pets] = useState<Pet[]>([
    { id: 1, name: 'Bella', breed: 'Labrador', age: 3, description: 'Friendly and energetic.', image: '/images/labrador.png' },
    { id: 2, name: 'Max', breed: 'Golden Retriever', age: 5, description: 'Loyal and calm.', image: '/images/Golden Retriever.png' },
    { id: 3, name: 'Lucy', breed: 'Bulldog', age: 2, description: 'Playful and loving.', image: '/images/Bulldog.png' },
  ]);

  const [selectedPet, setSelectedPet] = useState<Pet | null>(null);
  const [searchTerm, setSearchTerm] = useState<string>("");

  const handleViewDetails = (pet: Pet) => {
    setSelectedPet(pet);
  };

  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const filteredPets = pets.filter((pet) =>
    pet.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    pet.breed.toLowerCase().includes(searchTerm.toLowerCase()) ||
    pet.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Pets Page</h1>
      <p>This is where you can browse all available pets for adoption.</p>

      {/* Search Bar */}
      <input 
        type="text" 
        placeholder="Search by name, breed, or description..." 
        value={searchTerm} 
        onChange={handleSearch} 
        style={{
          padding: '0.5rem',
          width: '100%',
          maxWidth: '400px',
          marginBottom: '1rem',
          borderRadius: '5px',
          border: '1px solid #ccc',
        }}
      />

      {/* Main Content Area with Flex Layout */}
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '2rem' }}>
        
        {/* Pet List Section */}
        <div style={{ flex: 1 }}>
          {filteredPets.length > 0 ? (
            filteredPets.map((pet) => (
              <div key={pet.id} style={{ marginBottom: '1rem', textAlign: 'center', display: 'flex', alignItems: 'center' }}>
                <img 
                  src={pet.image} 
                  alt={`${pet.name}`} 
                  style={{ 
                    width: '100px',  
                    height: '100px',  
                    borderRadius: '50%', 
                    marginRight: '1rem' 
                  }} 
                />
                <span>{pet.name}</span>
                <button onClick={() => handleViewDetails(pet)} style={{ marginLeft: '6rem' }}>
                  View Details
                </button>
              </div>
            ))
          ) : (
            <p>No pets found at this moment :/</p>
          )}
        </div>

        {/* Pet Details Section */}
        <div style={{ flex: '0 0 300px', padding: '1rem', borderRadius: '8px' }}>
          {selectedPet ? (
            <>
              <h2>{selectedPet.name}</h2>
              <p><strong>Breed:</strong> {selectedPet.breed}</p>
              <p><strong>Age:</strong> {selectedPet.age}</p>
              <p><strong>Description:</strong> {selectedPet.description}</p>
              <button onClick={() => setSelectedPet(null)}>
                Close
              </button>
            </>
          ) : (
            <p> </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Pets;
