import React, { useState } from 'react';
import { Box, Modal, TextField, Button, Typography } from '@mui/material';
import axios from 'axios';

const AuthModal = ({ open, onClose, onLoginSuccess }) => {
  const [formData, setFormData] = useState({ id_usuario: '', password: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        'http://localhost:8000/auth/login',
        {
          username: formData.id_usuario,
          password: formData.password
        },
        { headers: { 'Content-Type': 'application/json' } }
      );

      if (res.data && res.data.access_token) {
        localStorage.setItem('token', res.data.access_token);
        alert('Login exitoso');

        // Llamamos al callback para actualizar App.jsx
        onLoginSuccess(formData.id_usuario);

        // Cerramos el modal
        onClose();
      } else {
        alert('Credenciales incorrectas');
      }
    } catch (error) {
      console.error(error);
      alert('Error al conectar con el servidor');
    }
  };

  return (
    <Modal open={open} onClose={onClose}>
      <Box sx={{
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: '#1e1e1e',
        boxShadow: 24,
        p: 4,
        borderRadius: 2,
        color: 'white'
      }}>
        <Typography variant="h6" mb={2} sx={{ color: '#ffcc00' }}>
          Iniciar Sesión
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="ID de Usuario"
            name="id_usuario"
            value={formData.id_usuario}
            onChange={handleChange}
            margin="normal"
            required
            InputLabelProps={{ style: { color: '#bbb' } }}
            InputProps={{ style: { color: 'white' } }}
          />
          <TextField
            fullWidth
            label="Contraseña"
            name="password"
            type="password"
            value={formData.password}
            onChange={handleChange}
            margin="normal"
            required
            InputLabelProps={{ style: { color: '#bbb' } }}
            InputProps={{ style: { color: 'white' } }}
          />
          <Box mt={3}>
            <Button
              type="submit"
              variant="contained"
              fullWidth
              sx={{
                backgroundColor: '#ffcc00',
                color: '#000',
                '&:hover': { backgroundColor: '#e6b800' }
              }}
            >
              Iniciar Sesión
            </Button>
          </Box>
        </form>
      </Box>
    </Modal>
  );
};

export default AuthModal;