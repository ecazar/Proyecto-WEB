// // import { useState } from 'react'
// // import reactLogo from './assets/react.svg'
// // import viteLogo from '/vite.svg'
// // import './App.css'

// // function App() {
// //   const [count, setCount] = useState(0)

// //   return (
// //     <>
// //       <div>
// //         <a href="https://vite.dev" target="_blank">
// //           <img src={viteLogo} className="logo" alt="Vite logo" />
// //         </a>
// //         <a href="https://react.dev" target="_blank">
// //           <img src={reactLogo} className="logo react" alt="React logo" />
// //         </a>
// //       </div>
// //       <h1>Vite + React</h1>
// //       <div className="card">
// //         <button onClick={() => setCount((count) => count + 1)}>
// //           count is {count}
// //         </button>
// //         <p>
// //           Edit <code>src/App.jsx</code> and save to test HMR
// //         </p>
// //       </div>
// //       <p className="read-the-docs">
// //         Click on the Vite and React logos to learn more
// //       </p>
// //     </>
// //   )
// // }

// // export default App

// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
// import Home from './pages/Home'
// // import Login from './pages/Login'
// // import Register from './pages/Register'
// // import Dashboard from './pages/Dashboard'

// function App() {
//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<Home />} />
//         {/* <Route path="/login" element={<Login />} /> */}
//         {/* <Route path="/register" element={<Register />} /> */}
//         {/* <Route path="/dashboard" element={<Dashboard />} /> */}
//       </Routes>
//     </Router>
//   )
// }

// export default App


// src/App.jsx
import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
// import Login from './pages/Login'
import ConsultarLibros from './pages/ConsultarLibros'
import MisLibros from './pages/MisLibros'
import ConsultarMultas from './pages/ConsultarMultas'
import AuthModal from './components/AuthModal'

function App() {
  const [authOpen, setAuthOpen] = useState(false)

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
            <button onClick={() => setAuthOpen(true)}>Login</button>
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

      {/* Modal */}
      <AuthModal open={authOpen} onClose={() => setAuthOpen(false)} />

    </Router>
  )
}

export default App