// src/components/Navbar.tsx

import React from "react";
import { Link } from "react-router-dom";

const Navbar: React.FC = () => {
  return (
    <header>
      <nav className="navbar">
        <div className="navbar-left">
          <Link to="/" className="navbar-logo">
            <img src="images/pet_adoption_logo.png" alt="Home" className="navbar-icon" />
          </Link>

          <Link to="/pets">Pets</Link>
          <Link to="/contact">Contact Us</Link>
        </div>
        <div className="navbar-right">
          
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
