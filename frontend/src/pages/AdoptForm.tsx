
import React, {useEffect, useState } from "react";
import './AdoptForm.css';
import { useNavigate } from 'react-router-dom';


const AdoptForm: React.FC = () => {
  // Get the user_id from localStorage
  const user_id = localStorage.getItem('user_id');
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!user_id) {
      alert(`Login required!`);
      navigate('/login');  // Redirect to login page if not logged in
    }
  }, [navigate, user_id]);

  const [formData, setFormData] = useState({
    name: "",
    salary: "",
    housing:"",
    contact:"",
    pet_name:"",
  });
 
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    const { name, salary, housing, contact, pet_name } = formData;
    if (!name || !salary || !housing || !contact || !pet_name) {
      console.error("All fields must be filled out.");
      return;
    }
    try {
      const response = await fetch(`/form`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      if (response.ok) {
        alert('Form submited!');
        navigate('/dashboard'); // Redirect to dashboard
      } else {
        setError(data.error);
      }
    } catch (err) {
      console.error('Error submitting form:', err);
      setError('An unexpected error occurred');
    }
  };




  return (
    <div>
      <h1>Pet Adoption Form</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={formData.name}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Montly Salary:</label>
          <input
            type="number"
            value={formData.salary}
            onChange={(e) => setFormData({ ...formData, salary: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Do you own or rent a place:</label>
          <input
            type="text"
            value={formData.housing}
            onChange={(e) => setFormData({ ...formData, housing: e.target.value })}
            required
          />
        </div>
        <div>
          <label>What is your email address?</label>
          <input
            type="text"
            value={formData.contact}
            onChange={(e) => setFormData({ ...formData, contact: e.target.value })}
            required
          />
        </div>
        <div>
        <label>Name of the pet that you want to adopt:</label>
        <input
            type="text"
            value={formData.pet_name}
            onChange={(e) => setFormData({ ...formData, pet_name: e.target.value })}
            required
          />
        </div>
        <button type="submit">Submit Form</button>
      </form>
       {/* Display the error message if it exists */}
       {error && <div className="error">{error}</div>}
    </div>

  );
};

export default AdoptForm;
