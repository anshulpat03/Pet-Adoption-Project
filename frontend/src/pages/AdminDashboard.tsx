import React, { useState } from "react";
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

export default AdminDashboard;
