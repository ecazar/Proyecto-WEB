from pydantic import BaseModel
from typing import Optional, List

class LibroBase(BaseModel):
    isbn: str
    titulo: str
    autor: str
    paginas: Optional[int]
    portada_uri: Optional[str]

class LibroCreate(LibroBase):
    total_ejemplares: int

class LibroOut(LibroBase):
    id: int
    total_ejemplares: int
    disponibles: int

    class Config:
        orm_mode = True

class RecomendacionBase(BaseModel):
    comentario: Optional[str]

class RecomendacionCreate(RecomendacionBase):
    origen_id: int
    recomendado_id: int

class RecomendacionOut(RecomendacionBase):
    id: int
    origen_id: int
    recomendado_id: int

    class Config:
        orm_mode = True
