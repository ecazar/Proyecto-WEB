import { useEffect, useState } from 'react'
import axios from 'axios'


function ConsultarMultas() {
  const [multas, setMultas] = useState([])

  useEffect(() => {
    const token = localStorage.getItem('token')
    const userId = 1 // <- reemplaza con el id real

    axios.get(`http://localhost:8000/multas/usuario/${userId}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(res => setMultas([res.data])) // devuelve solo una multa, lo pongo en array
    .catch(err => console.error('Error al obtener multas:', err))
  }, [])

  return (
    <div className="table-container">
      <h2 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '16px' }}>Historial de Multas</h2>
      <table>
        <thead>
          <tr>
            <th>Usuario</th>
            <th>Inicio</th>
            <th>Días Acumulados</th>
            <th>Finalización</th>
          </tr>
        </thead>
        <tbody>
          {multas.map((multa, i) => (
            <tr key={i}>
              <td>{multa.usuario}</td>
              <td>{multa.fecha_inicio}</td>
              <td>{multa.dias_acumulados}</td>
              <td>{multa.fecha_finalizacion || 'En curso'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default ConsultarMultas
