import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar.tsx"
import './App.css'
import Pets from "./pages/Pets.tsx";
import Home from "./pages/Home.tsx";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/pets" element={<Pets />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
