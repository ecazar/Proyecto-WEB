import { useEffect, useState } from 'react'
import axios from 'axios'

function MisLibros() {
  const [ejemplares, setEjemplares] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/mis-libros')
      .then(res => setEjemplares(res.data))
  }, [])

  return (
    <div className="table-container">
      <h2 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '16px' }}>Mis Libros Prestados</h2>
      <table>
        <thead>
          <tr>
            <th>Código Ejemplar</th>
            <th>ID Libro</th>
            <th>Fecha Adquisición</th>
            <th>Estado</th>
            <th>Préstamo</th>
            <th>Devolución</th>
          </tr>
        </thead>
        <tbody>
          {ejemplares.map(ej => (
            <tr key={ej.codigo}>
              <td>{ej.codigo}</td>
              <td>{ej.id_libro}</td>
              <td>{ej.fecha_adquisicion}</td>
              <td>{ej.observaciones}</td>
              <td>{ej.fecha_prestamo}</td>
              <td>{ej.fecha_devolucion}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default MisLibros
