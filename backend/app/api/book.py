from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
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

@router.get("/", response_model=List[LibroOut])
async def listar_libros(db: AsyncSession = Depends(get_db)):
    return await crud_book.get_all_libros(db)

@router.get("/{id}", response_model=LibroOut)
async def obtener_libro(id: int, db: AsyncSession = Depends(get_db)):
    return await crud_book.get_libro_by_id(db, id)

@router.get("/{id}/recomendaciones", response_model=List[RecomendacionOut])
async def recomendaciones_libro(id: int, db: AsyncSession = Depends(get_db)):
    return await crud_book.get_recomendaciones_por_libro(db, id)