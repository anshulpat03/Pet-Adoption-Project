import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar.tsx"
import './App.css'
import Pets from "./pages/Pets.tsx";
import Home from "./pages/Home.tsx";
import Contact from "./components/Contact.tsx";
import { useState } from "react";

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
        </Routes>
      </Router>
      <Contact isOpen={isContactOpen} onClose={handleCloseContact} />
    </>
  )
}

export default App
