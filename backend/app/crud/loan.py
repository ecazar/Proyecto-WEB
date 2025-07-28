from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.loan import Prestamo, HistoricoPrestamo
from app.models.copy import Ejemplar
from app.models.book import Libro
from app.schemas.loan import PrestamoCreate

async def create_prestamo(db: AsyncSession, prestamo_data: PrestamoCreate):
    prestamo = Prestamo(**prestamo_data.dict())
    db.add(prestamo)

    # Reducir ejemplares disponibles
    ejemplar = await db.get(Ejemplar, prestamo.ejemplar_id)
    if ejemplar:
        libro = await db.get(Libro, ejemplar.libro_id)
        if libro:
            libro.disponibles -= 1

    await db.commit()
    await db.refresh(prestamo)
    return prestamo

async def get_prestamos_por_usuario(db: AsyncSession, usuario_id: int):
    result = await db.execute(select(Prestamo).where(Prestamo.usuario_id == usuario_id))
    return result.scalars().all()

async def get_historico_prestamos_usuario(db: AsyncSession, usuario_id: int):
    result = await db.execute(
        select(HistoricoPrestamo).where(HistoricoPrestamo.usuario_id == usuario_id)
    )
    return result.scalars().all()

async def devolver_prestamo(db: AsyncSession, prestamo_id: int, fecha_devolucion: any):
    result = await db.execute(select(Prestamo).where(Prestamo.id == prestamo_id))
    prestamo = result.scalar_one_or_none()

    if not prestamo:
        return None

    historico = HistoricoPrestamo(
        usuario_id=prestamo.usuario_id,
        ejemplar_id=prestamo.ejemplar_id,
        fecha_prestamo=prestamo.fecha_prestamo,
        fecha_devolucion=fecha_devolucion
    )
    db.add(historico)

    # Aumentar ejemplares disponibles
    ejemplar = await db.get(Ejemplar, prestamo.ejemplar_id)
    if ejemplar:
        libro = await db.get(Libro, ejemplar.libro_id)
        if libro:
            libro.disponibles += 1

    await db.delete(prestamo)
    await db.commit()
    return historico
