import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar.tsx"
import './App.css'
import Pets from "./pages/Pets.tsx";
import Home from "./pages/Home.tsx";
import AdminPage from './pages/AdminPage'; 
import Login from "./pages/Login.tsx";


function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/pets" element={<Pets />} />
          <Route path="/admin" element={<AdminPage />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
