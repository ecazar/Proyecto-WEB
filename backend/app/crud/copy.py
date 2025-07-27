from sqlalchemy.ext.asyncio import AsyncSession
from app.models.copy import Ejemplar
from app.schemas.copy import EjemplarCreate

async def create_ejemplar(db: AsyncSession, ejemplar_data: EjemplarCreate):
    ejemplar = Ejemplar(**ejemplar_data.dict())
    db.add(ejemplar)
    await db.commit()
    await db.refresh(ejemplar)
    return ejemplar
