// src/components/Navbar.tsx

import React from "react";
import { Link } from "react-router-dom";

const Navbar: React.FC = () => {
  return (
    <header>
      <nav className="navbar">
        <div className="navbar-left">
          <Link to="/" className="navbar-logo">
            <img src="/pet_adoption_logo.svg" alt="Home" className="navbar-icon" />
          </Link>

          <Link to="/pets">Pets</Link>
        </div>
        <div className="navbar-right">
          <Link to="/contact">Contact Us</Link>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
