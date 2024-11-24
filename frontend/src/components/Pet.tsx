import React from "react";

interface PetProps {
  pet: {
    id: number;
    name: string;
    breed: string;
    age: number;
    description: string;
    image: string;
  };
  onViewDetails: (pet: PetProps['pet']) => void;
}

const Pet: React.FC<PetProps> = ({ pet, onViewDetails }) => {
  return (
    <div style={{ marginBottom: '1rem', textAlign: 'center', display: 'flex', alignItems: 'center' }}>
      <img
        src={pet.image}
        alt={pet.name}
        style={{
          width: '100px',
          height: '100px',
          borderRadius: '50%',
          marginRight: '1rem',
        }}
      />
      <span>{pet.name}</span>
      <button onClick={() => onViewDetails(pet)} style={{ marginLeft: '1rem' }}>
        View Details
      </button>
    </div>
  );
};

export default Pet;
