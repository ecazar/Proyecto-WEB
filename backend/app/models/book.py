from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True, nullable=False)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    paginas = Column(Integer)
    total_ejemplares = Column(Integer, default=0)
    disponibles = Column(Integer, default=0)
    portada_uri = Column(String)

    ejemplares = relationship("Ejemplar", back_populates="libro")
    recomendaciones_origen = relationship("Recomendacion", back_populates="origen", foreign_keys="[Recomendacion.origen_id]")
    recomendaciones_destino = relationship("Recomendacion", back_populates="recomendado", foreign_keys="[Recomendacion.recomendado_id]")

class Recomendacion(Base):
    __tablename__ = "recomendaciones"

    id = Column(Integer, primary_key=True)
    origen_id = Column(Integer, ForeignKey("libros.id"))
    recomendado_id = Column(Integer, ForeignKey("libros.id"))
    comentario = Column(String)

    origen = relationship("Libro", back_populates="recomendaciones_origen", foreign_keys=[origen_id])
    recomendado = relationship("Libro", back_populates="recomendaciones_destino", foreign_keys=[recomendado_id])
