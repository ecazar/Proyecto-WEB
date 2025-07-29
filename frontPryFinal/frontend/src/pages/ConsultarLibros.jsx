import { useEffect, useState } from 'react'
import axios from 'axios'

function ConsultarLibros() {
  const [libros, setLibros] = useState([])

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) return

    axios.get('http://localhost:8000/libros', {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => setLibros(res.data))
    .catch(err => console.error('Error al obtener libros:', err))
  }, [])

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-6 text-center">Catálogo de Libros</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {libros.map(libro => (
          <div
            key={libro.isbn}
            className="border p-4 rounded shadow flex flex-col h-full hover:shadow-lg transition-shadow"
          >
            <div
              style={{
                width: '100%',
                height: '240px',        // altura fija uniforme
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                background: '#f9f9f9',
                marginBottom: '1rem',
                overflow: 'hidden',
                borderRadius: '4px'
              }}
            >
              <img
                src={libro.portada_uri}
                alt={libro.titulo}
                style={{
                  maxHeight: '100%',
                  maxWidth: '100%',
                  objectFit: 'contain'
                }}
              />
            </div>
            <h3 className="font-bold text-lg mb-1">{libro.titulo}</h3>
            <p className="text-gray-700 text-sm mb-1">Autor: {libro.autor}</p>
            <p className="text-gray-700 text-sm mb-1">Páginas: {libro.paginas}</p>
            <p className="text-gray-700 text-sm mb-1">Ejemplares: {libro.total_ejemplares}</p>
            <p className="text-gray-700 text-sm">Disponibles: {libro.disponibles}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ConsultarLibros
