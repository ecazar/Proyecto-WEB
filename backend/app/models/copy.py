from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Ejemplar(Base):
    __tablename__ = "ejemplares"

    id = Column(Integer, primary_key=True) 
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    fecha_adquisicion = Column(Date)
    codigo = Column(String)
    observaciones = Column(String)

    libro = relationship("Libro", back_populates="ejemplares")
    prestamos = relationship("Prestamo", back_populates="ejemplar")
