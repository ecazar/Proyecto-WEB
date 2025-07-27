from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ejemplar_id = Column(Integer, ForeignKey("ejemplares.id"), nullable=False)
    fecha_prestamo = Column(Date)
    fecha_devolucion_esperada = Column(Date)

    usuario = relationship("Usuario", back_populates="prestamos")
    ejemplar = relationship("Ejemplar", back_populates="prestamos")
