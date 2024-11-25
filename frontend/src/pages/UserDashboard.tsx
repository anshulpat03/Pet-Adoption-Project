import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const UserDashboard: React.FC = () => {
  const [userData, setUserData] = useState<any>(null); // eslint-disable-line
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  // Get the user_id from localStorage
  const user_id = localStorage.getItem('user_id');

  useEffect(() => {
    // If there's no user_id, redirect to login page
    if (!user_id) {
      setError('User not logged in');
      navigate('/login'); // Redirect to login page
      return;
    }

    // Fetch user data using user_id
    const fetchUserData = async () => {

        try {
            const response = await fetch(`/api/users/${user_id}`, {
              method: 'GET',
              headers: {
                'Content-Type': 'application/json',
              },
            });
        const data = await response.json();

        if (response.ok) {
          setUserData(data); // Set user data if the response is successful
        } else {
          setError(data.error || 'An error occurred while fetching user data.');
        }
      } catch (err) {
        console.error('Error fetching user data:', err);
        setError('An unexpected error occurred.');
      }
    };

    fetchUserData();
  }, [user_id, navigate]); // Re-run the effect if user_id or navigate changes

  // If no user data is available
  if (!userData) {
    return <div>User not found...</div>;
  }

  return (
    <div className="dashboard-container">
      <div className="dashboard-content">
        <h1>User Dashboard</h1>
        {error && <p className="error-message">{error}</p>}
        <div className="user-info">
          <p><strong>Email:</strong> {userData.email}</p>
          <p><strong>Name:</strong> {userData.username}</p>
          <p><strong>User ID:</strong> {userData.id}</p>
        </div>
        <button className="logout-button" onClick={() => {
          // Clear localStorage on logout
          localStorage.removeItem('user_id');
          navigate('/login'); // Redirect to login page
        }}>
          Logout
        </button>
      </div>
    </div>
  );
};

export default UserDashboard;
