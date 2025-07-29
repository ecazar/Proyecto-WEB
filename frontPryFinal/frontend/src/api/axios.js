// src/api/axios.js
import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true
})

export default instance


// Usar en cualquier componente de la siguiente manera
// import api from '../api/axios'

// api.get('/libros').then(res => ...)
