from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date
from app.schemas.common import EstadoUsuarioEnum, Direccion

class UsuarioBase(BaseModel):
    login: str
    nombre: str
    apellidos: str
    correo: EmailStr
    direccion: Direccion
    estado: EstadoUsuarioEnum = EstadoUsuarioEnum.activo

class UsuarioCreate(UsuarioBase):
    password: str
    tipo: str  # 'alumno' o 'profesor'

class UsuarioOut(UsuarioBase):
    id: int
    tipo: str

    class Config:
        orm_mode = True

class AlumnoExtra(BaseModel):
    telefono_padres: Optional[str]

class ProfesorExtra(BaseModel):
    departamento: Optional[str]
