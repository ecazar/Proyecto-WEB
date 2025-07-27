from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.book import LibroCreate, LibroOut, RecomendacionCreate, RecomendacionOut
from app.crud import book as crud_book
from app.db.session import SessionLocal

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=LibroOut)
async def crear_libro(libro: LibroCreate, db: AsyncSession = Depends(get_db)):
    return await crud_book.create_libro(db, libro)

@router.post("/recomendaciones", response_model=RecomendacionOut)
async def crear_recomendacion(rec: RecomendacionCreate, db: AsyncSession = Depends(get_db)):
    return await crud_book.create_recomendacion(db, rec)
