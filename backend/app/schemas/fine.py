from pydantic import BaseModel
from datetime import date
from typing import Optional

class MultaBase(BaseModel):
    fecha_inicio: date
    dias_acumulados: int
    fecha_fin: Optional[date] = None

class MultaCreate(MultaBase):
    usuario_id: int

class MultaOut(MultaBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True

class HistoricoMulta(BaseModel):
    usuario_id: int
    fecha_inicio: date
    fecha_fin: date
    dias_acumulados: int