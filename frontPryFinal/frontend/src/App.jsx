import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import ConsultarLibros from './pages/ConsultarLibros'
import MisLibros from './pages/MisLibros'
import ConsultarMultas from './pages/ConsultarMultas'
import AuthModal from './components/AuthModal'

function App() {
  const [authOpen, setAuthOpen] = useState(false)
  const [username, setUsername] = useState(null)

  return (
    <Router>
      <header className="main-header">
        <div className="header-container">
          <h1 className="site-title">Biblioteca</h1>
          <nav className="nav-links">
            <Link to="/">Home</Link>
            <Link to="/consultar-libros">Consultar Libros</Link>
            <Link to="/mis-libros">Mis Libros</Link>
            <Link to="/consultar-multas">Consultar Multas</Link>
            {username ? (
              <span>Hola, {username} 👋</span>
            ) : (
              <button onClick={() => setAuthOpen(true)}>Login</button>
            )}
          </nav>
        </div>
      </header>

      <main className="p-6">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/consultar-libros" element={<ConsultarLibros />} />
          <Route path="/mis-libros" element={<MisLibros />} />
          <Route path="/consultar-multas" element={<ConsultarMultas />} />
        </Routes>
      </main>

      <AuthModal
        open={authOpen}
        onClose={() => setAuthOpen(false)}
        onLoginSuccess={(user) => setUsername(user)}
      />
    </Router>
  )
}

export default App
