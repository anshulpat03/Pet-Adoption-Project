import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'; // For navigation to another page

interface User {
  id: number;
  username: string;
  email: string;
  adoption_status: string;
}

const AdminPage: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate(); // Initialize navigation

  // Fetch users from backend
  useEffect(() => {
    fetch('/api/users') // Ensure this matches your backend API
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch user data');
        }
        return response.json();
      })
      .then((data) => {
        setUsers(data.slice(0, 3)); // Use only the first 3 users
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading users...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  // Image mapping for each user
  const userImages = [
    '/images/Profile_1.png',
    '/images/Profile_2.png',
    '/images/Profile_3.png',
  ];

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Admin Dashboard</h1>
      <h2>User Profiles and Adoption Progress</h2>
      <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', justifyContent: 'center' }}>
        {users.map((user, index) => (
          <div
            key={user.id}
            style={{
              border: '1px solid #ccc',
              borderRadius: '8px',
              padding: '1rem',
              width: '250px',
              textAlign: 'center',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center', // Center-align content
            }}
          >
            <img
              src={userImages[index]} // Match user to image by index
              alt={`${user.username}'s profile`}
              style={{
                width: '150px', // Set fixed width for consistent size
                height: '150px', // Set fixed height for consistent size
                objectFit: 'cover',
                borderRadius: '50%', // Circular image
                marginBottom: '1rem', // Add spacing below image
              }}
            />
            <h3>{user.username}</h3>
            <p>Email: {user.email}</p>
            <p>Status: {user.adoption_status}</p>
            <button
              onClick={() => navigate(`/adoption-form/${user.id}`)} // Navigate to the adoption form page
              style={{
                marginTop: '1rem',
                padding: '0.5rem 1rem',
                backgroundColor: '#007BFF',
                color: '#fff',
                border: 'none',
                borderRadius: '5px',
                cursor: 'pointer',
              }}
            >
              Adoption Form
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AdminPage;
