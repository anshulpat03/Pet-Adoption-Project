// src/components/Navbar.tsx

import React from "react";
import { Link } from "react-router-dom";

interface NavbarProps {
  onContactClick: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ onContactClick }) => {
  return (
    <header>
      <nav className="navbar">
        <div className="navbar-left">
          <Link to="/" className="navbar-logo">
            <img src="images/pet_adoption_logo.png" alt="Home" className="navbar-icon" />
          </Link>
          <Link to="/pets">Pets</Link>
          <Link to="/admin">Admin Dashboard</Link>
          <Link to="/form">Adoption Form</Link>
          <span className="navbar-contact" onClick={onContactClick}>
            Contact Us
          </span>
        </div>
        <div className="navbar-right">
        <Link to="/dashboard">User Dashboard</Link>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
