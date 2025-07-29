import { useEffect, useState } from 'react'
import axios from 'axios'

function ConsultarMultas() {
  const [multas, setMultas] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/multas')
      .then(res => setMultas(res.data))
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
