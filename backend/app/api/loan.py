from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.loan import PrestamoCreate, PrestamoOut
from app.crud import loan as crud_loan
from app.db.session import SessionLocal
from typing import List

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=PrestamoOut)
async def crear_prestamo(prestamo: PrestamoCreate, db: AsyncSession = Depends(get_db)):
    return await crud_loan.create_prestamo(db, prestamo)

@router.get("/usuario/{usuario_id}", response_model=List[PrestamoOut])
async def prestamos_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    return await crud_loan.get_prestamos_por_usuario(db, usuario_id)
