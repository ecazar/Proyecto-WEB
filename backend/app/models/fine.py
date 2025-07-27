from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class Multa(Base):
    __tablename__ = "multas"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_inicio = Column(Date)
    dias_acumulados = Column(Integer, default=0)
    fecha_fin = Column(Date, nullable=True)

    usuario = relationship("Usuario", back_populates="multa_actual")

class HistoricoMulta(Base):
    __tablename__ = "historico_multas"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    dias_acumulados = Column(Integer)

class HistoricoPrestamo(Base):
    __tablename__ = "historico_prestamos"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer)
    ejemplar_id = Column(Integer)
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)
