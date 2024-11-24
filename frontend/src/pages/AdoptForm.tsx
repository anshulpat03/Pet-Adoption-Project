
import React, { useState, useEffect } from "react";
//import { useParams } from "react-router-dom";

const AdoptForm: React.FC = () => {
  //const { user_id } = useParams<{ user_id: string }>();  // Get the user_id from the URL params 

  useEffect(() => {
    console.log("Pet Adoption Form"); 
  });

  const [formData, setFormData] = useState({
    name: "",
    salary: "",
    housing:"",
    contact:"",
    pet_name:"",
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const { name, salary, housing, contact, pet_name } = formData;
    if (!name || !salary || !housing || !contact || !pet_name) {
      console.error("All fields must be filled out.");
      return;
    }

    const response = await fetch(`/form`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });
    const responseData = await response.json();
    console.log(responseData);  // Handle the response from the backend
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
    </div>
  );
};

export default AdoptForm;
