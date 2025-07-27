from sqlalchemy.ext.asyncio import AsyncSession
from app.models.fine import Multa
from app.schemas.fine import MultaCreate

async def create_multa(db: AsyncSession, multa_data: MultaCreate):
    multa = Multa(**multa_data.dict())
    db.add(multa)
    await db.commit()
    await db.refresh(multa)
    return multa

async def get_multa_por_usuario(db: AsyncSession, usuario_id: int):
    result = await db.execute(
        select(Multa).where(Multa.usuario_id == usuario_id)
    )
    return result.scalars().first()
