import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();
      console.log("Server response:", data);
      if (response.ok) {
        console.log('user_id:', data.user_id);
        localStorage.setItem('user_id', data.user_id);
        alert(`Welcome back!`);
        navigate(`/dashboard`); // Redirect to dashboard
      } else {
        setError(data.error);
      }
    } catch (err) {
      console.error('Error logging in:', err);
      setError('An unexpected error occurred');
    }
  };

  return (
    <div
      style={{
        backgroundImage: `url('./images/login.png')`, // Replace with your image path
        backgroundSize: 'cover', // Ensure the image covers the entire viewport
        backgroundPosition: 'center', // Center the image
        backgroundRepeat: 'no-repeat', // Prevent image tiling
        height: '100vh', // Cover the entire viewport height
        width: '100vw', // Cover the entire viewport width
        display: 'flex', // Center the form horizontally and vertically
        justifyContent: 'center',
        alignItems: 'center',
        margin: 0, // Remove any default margin
        padding: 0, // Remove any default padding
        overflow: 'hidden', // Prevent scrollbars
      }}
    >
      <form
        onSubmit={handleSubmit}
        style={{
          background: 'rgba(255, 255, 255, 0.8)', // Semi-transparent white background
          padding: '2rem',
          borderRadius: '8px',
          boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
          width: '300px',
          textAlign: 'center',
        }}
      >
        <h1 style={{ marginBottom: '1rem' }}>Login</h1>
        <div style={{ marginBottom: '1rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px',
            }}
          />
        </div>
        <div style={{ marginBottom: '1rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px',
            }}
          />
        </div>
        <button
          type="submit"
          style={{
            background: '#007BFF',
            color: '#fff',
            padding: '0.5rem 1rem',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            width: '100%',
          }}
        >
          Login
        </button>
        {error && <p style={{ color: 'red', marginTop: '1rem' }}>{error}</p>}
      </form>
    </div>
  );
};

export default Login;
