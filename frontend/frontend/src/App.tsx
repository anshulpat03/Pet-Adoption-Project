import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar.tsx"
import './App.css'
import Pets from "./pages/Pets.tsx";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/pets" element={<Pets />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
