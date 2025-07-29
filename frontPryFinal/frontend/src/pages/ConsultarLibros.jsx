// src/pages/ConsultarLibros.jsx
import { useEffect, useState } from 'react'
import axios from 'axios'

function ConsultarLibros() {
  const [libros, setLibros] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/libros')
      .then(res => setLibros(res.data))
  }, [])

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Catálogo de Libros</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {libros.map(libro => (
          <div key={libro.isbn} className="border p-4 rounded shadow">
            <img src={libro.portada_uri} alt={libro.titulo} className="w-full h-48 object-cover mb-2" />
            <h3 className="font-bold">{libro.titulo}</h3>
            <p>Autor: {libro.autor}</p>
            <p>Páginas: {libro.paginas}</p>
            <p>Ejemplares: {libro.ejemplares_comprados}</p>
            <p>Disponibles: {libro.ejemplares_disponibles}</p>
          </div>
        ))}
      </div>
      {/* Recomendaciones */}
      <h3 className="text-xl font-semibold mt-8 mb-2">Recomendaciones</h3>
      <ul className="list-disc list-inside">
        <li>Libro recomendado 1</li>
        <li>Libro recomendado 2</li>
      </ul>
    </div>
  )
}

export default ConsultarLibros