from sqlalchemy.ext.asyncio import AsyncSession
from app.models.loan import Prestamo
from app.schemas.loan import PrestamoCreate
from sqlalchemy import select


async def create_prestamo(db: AsyncSession, prestamo_data: PrestamoCreate):
    prestamo = Prestamo(**prestamo_data.dict())
    db.add(prestamo)
    await db.commit()
    await db.refresh(prestamo)
    return prestamo

async def get_prestamos_por_usuario(db: AsyncSession, usuario_id: int):
    result = await db.execute(select(Prestamo).where(Prestamo.usuario_id == usuario_id))
    return result.scalars().all()
