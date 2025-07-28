from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from pydantic import BaseModel
from typing import Optional
from app.schemas.common import Direccion as DireccionSchema

import enum

class EstadoUsuarioEnum(str, enum.Enum):
    activo = "activo"
    moroso = "moroso"
    multado = "multado"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)  # alumno o profesor
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    correo = Column(String, nullable=False)

    calle = Column(String)
    numero = Column(String)
    piso = Column(String)
    ciudad = Column(String)
    codigo_postal = Column(String)

    estado = Column(Enum(EstadoUsuarioEnum), default=EstadoUsuarioEnum.activo)

    prestamos = relationship("Prestamo", back_populates="usuario")
    multa_actual = relationship("Multa", back_populates="usuario", uselist=False)

    alumno = relationship("Alumno", back_populates="usuario", uselist=False)
    profesor = relationship("Profesor", back_populates="usuario", uselist=False)

    @property
    def direccion(self) -> DireccionSchema:
        return DireccionSchema(
            calle=self.calle,
            numero=self.numero,
            piso=self.piso,
            ciudad=self.ciudad,
            codigo_postal=self.codigo_postal
        )

class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    telefono_padres = Column(String, nullable=True)

    usuario = relationship("Usuario", back_populates="alumno")

class Profesor(Base):
    __tablename__ = "profesores"
    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    departamento = Column(String, nullable=True)

    usuario = relationship("Usuario", back_populates="profesor")

class UsuarioToken(BaseModel):
    id: int
    login: str
    rol: str