from pydantic import BaseModel
from datetime import date


class PrestamoBase(BaseModel):
    fecha_prestamo: date
    fecha_devolucion_esperada: date

class PrestamoCreate(PrestamoBase):
    usuario_id: int
    ejemplar_id: int

class PrestamoOut(PrestamoBase):
    id: int
    usuario_id: int
    ejemplar_id: int

    class Config:
        orm_mode = True

class HistoricoPrestamo(BaseModel):
    usuario_id: int
    ejemplar_id: int
    fecha_prestamo: date
    fecha_devolucion: date

class HistoricoPrestamoOut(HistoricoPrestamo):
    id: int

    class Config:
        from_attributes = True
