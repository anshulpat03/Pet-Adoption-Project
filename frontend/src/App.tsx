import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar.tsx"
import './App.css'
import Pets from "./pages/Pets.tsx";
import Home from "./pages/Home.tsx";
import Login from "./pages/Login.tsx";
import Contact from "./components/Contact.tsx";
import { useState } from "react";
import AdminDashboard from "./pages/AdminDashboard.tsx";
import AdoptForm from "./pages/AdoptForm.tsx";
import UserDashboard from "./pages/UserDashboard.tsx";

function App() {
  const [isContactOpen, setIsContactOpen] = useState(false);

  const handleOpenContact = () => setIsContactOpen(true);
  const handleCloseContact = () => setIsContactOpen(false);
  return (
    <>
      <Router>
        <Navbar onContactClick={handleOpenContact}/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/pets" element={<Pets />} />
          
          <Route path="/login" element={<Login />} />
          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/form" element={<AdoptForm />} />
          <Route path="/dashboard" element={<UserDashboard />} />
        </Routes>
      </Router>
      <Contact isOpen={isContactOpen} onClose={handleCloseContact} />
    </>
  )
}

export default App