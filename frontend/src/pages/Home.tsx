import React from 'react';
import Button from '../components/Button';
import { useNavigate } from 'react-router-dom';

const Home: React.FC = () => {
  const navigate = useNavigate();

  const handleButtonClick = (destination: string) => {
    console.log(`${destination} button clicked!`);
    navigate(destination);
  };

  return (
    <>
      <div className="banner"></div>
      <div className="landing-text">
        <div style={{ padding: '2rem', textAlign: 'start' }}>
          <h1>Find your new best friend!</h1>
          <p>
            We're here to help connect you with the perfect furry companion!
            Our mission is to make the adoption process easy and enjoyable,
            matching pets with loving homes. Whether you're looking for a
            playful puppy or a wise senior dog, we're excited to help you find
            your new best friend.
          </p>
        </div>
        <div className="button">
          <p>Each pet deserves a loving home—adopt today!</p>
          <Button label="Browse Pets" onClick={() => handleButtonClick('/pets')} />
        </div>
        <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
          <div className="button">
            <Button label="Admin Login" onClick={() => handleButtonClick('/admin')} />
          </div>
          <div className="button">
            <Button label="User Login" onClick={() => handleButtonClick('/login')} />
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
