from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.copy import EjemplarCreate, EjemplarOut
from app.crud import copy as crud_copy
from app.db.session import SessionLocal

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=EjemplarOut)
async def crear_ejemplar(ejemplar: EjemplarCreate, db: AsyncSession = Depends(get_db)):
    return await crud_copy.create_ejemplar(db, ejemplar)
