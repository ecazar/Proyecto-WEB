from pydantic import BaseModel
from datetime import date

class EjemplarBase(BaseModel):
    fecha_adquisicion: date
    codigo: str
    observaciones: str

class EjemplarCreate(EjemplarBase):
    libro_id: int

class EjemplarOut(EjemplarBase):
    id: int
    libro_id: int

    class Config:
        orm_mode = True
