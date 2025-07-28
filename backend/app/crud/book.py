from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.book import Libro, Recomendacion
from app.schemas.book import LibroCreate, RecomendacionCreate

async def create_libro(db: AsyncSession, libro_data: LibroCreate):
    libro = Libro(**libro_data.dict(), disponibles=libro_data.total_ejemplares)
    db.add(libro)
    await db.commit()
    await db.refresh(libro)
    return libro

async def get_libro_by_isbn(db: AsyncSession, isbn: str):
    result = await db.execute(select(Libro).where(Libro.isbn == isbn))
    return result.scalars().first()

async def create_recomendacion(db: AsyncSession, rec_data: RecomendacionCreate):
    recomendacion = Recomendacion(**rec_data.dict())
    db.add(recomendacion)
    await db.commit()
    await db.refresh(recomendacion)
    return recomendacion

async def get_all_libros(db: AsyncSession):
    result = await db.execute(select(Libro))
    return result.scalars().all()

async def get_libro_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Libro).where(Libro.id == id))
    return result.scalars().first()

async def get_recomendaciones_por_libro(db: AsyncSession, libro_id: int):
    result = await db.execute(select(Recomendacion).where(Recomendacion.origen_id == libro_id))
    return result.scalars().all()