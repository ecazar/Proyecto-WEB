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
