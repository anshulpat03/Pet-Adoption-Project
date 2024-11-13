import React from 'react';

const Pets: React.FC = () => {
  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Pets Page</h1>
      <p>This is where you can browse all available pets for adoption.</p>

      <div style={{ marginTop: '2rem', color: '#555' }}>
        <p>Loading available pets...</p>
      </div>
    </div>
  );
};

export default Pets