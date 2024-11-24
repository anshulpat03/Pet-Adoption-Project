/*import React, { useState } from "react";
import AddPetForm from "../components/AddPetForm";
import AdminPetList from "../components/AdminPetList";
import "./AdminDashboard.css";

const AdminDashboard: React.FC = () => {
  const [showAddPetPopup, setShowAddPetPopup] = useState(false);

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <button className="btn add-pet-btn" onClick={() => setShowAddPetPopup(true)}>
        Add Pet
      </button>

      {showAddPetPopup && (
        <div className="popup-overlay">
          <div className="popup-container">
            <AddPetForm onClose={() => setShowAddPetPopup(false)} />
          </div>
        </div>
      )}

      <div className="admin-pet-list">
        <AdminPetList />
      </div>
    </div>
  );
};

export default AdminDashboard;*/
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'; // For navigation
import AddPetForm from '../components/AddPetForm';
import AdminPetList from '../components/AdminPetList';
import './AdminDashboard.css';

// User interface
interface User {
  id: number;
  username: string;
  email: string;
  adoption_status: string;
}

const AdminDashboard: React.FC = () => {
  // User states
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Pet form popup state
  const [showAddPetPopup, setShowAddPetPopup] = useState(false);

  const navigate = useNavigate();

  // Fetch users
  useEffect(() => {
    fetch('/api/users') // Ensure this matches your backend API
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch user data');
        }
        return response.json();
      })
      .then((data) => {
        setUsers(data.slice(0, 3)); // Display only the first 3 users
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  // Handle loading and error states for users
  if (loading) {
    return <p>Loading users...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  // User images (mapped by index)
  const userImages = [
    '/images/Profile_1.png',
    '/images/Profile_2.png',
    '/images/Profile_3.png',
  ];

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>

      {/* User Profiles Section */}
      <h2>User Profiles and Adoption Progress</h2>
      <div
        style={{
          display: 'flex',
          gap: '1rem',
          flexWrap: 'wrap',
          justifyContent: 'center',
        }}
      >
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
              alignItems: 'center',
            }}
          >
            <img
              src={userImages[index]}
              alt={`${user.username}'s profile`}
              style={{
                width: '150px',
                height: '150px',
                objectFit: 'cover',
                borderRadius: '50%',
                marginBottom: '1rem',
              }}
            />
            <h3>{user.username}</h3>
            <p>Email: {user.email}</p>
            <p>Status: {user.adoption_status}</p>
            <button
              onClick={() => navigate(`/adoption-form/${user.id}`)}
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

      {/* Pet Management Section */}
      <h2>Pet Management</h2>
      <button
        className="btn add-pet-btn"
        onClick={() => setShowAddPetPopup(true)}
      >
        Add Pet
      </button>

      {showAddPetPopup && (
        <div className="popup-overlay">
          <div className="popup-container">
            <AddPetForm onClose={() => setShowAddPetPopup(false)} />
          </div>
        </div>
      )}

      <div className="admin-pet-list">
        <AdminPetList />
      </div>
    </div>
  );
};

export default AdminDashboard;

