from enum import Enum
from pydantic import BaseModel

class EstadoUsuarioEnum(str, Enum):
    activo = "activo"
    moroso = "moroso"
    multado = "multado"

class Direccion(BaseModel):
    calle: str
    numero: str
    piso: str | None = None
    ciudad: str
    codigo_postal: str
