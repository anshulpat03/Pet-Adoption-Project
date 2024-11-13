import React from 'react';
import Button from '../components/Button';
import { useNavigate } from 'react-router-dom';

const Home: React.FC = () => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    console.log('Button clicked!');
    navigate('/pets');  
  };
  return (
    <>
        <div className="banner"></div>  
        <div className='landing-text'>
            <div style={{ padding: '2rem', textAlign: 'start' }}>
                <h1>Find your new best friend!</h1>
                <p>We're here to help connect you with the perfect furry companion! 
                    Our mission is to make the adoption process easy and enjoyable, 
                    matching pets with loving homes. Whether you're looking for a playful puppy or a wise senior dog, 
                    we're excited to help you find your new best friend.</p>
            </div>
            <div className='button'>
                <p>Meet all the adorable friends waiting for their forever home!</p>
                <Button label="Browse Pets" onClick={handleButtonClick}/>
            </div>
        </div>
     </>
    
  );
};

export default Home