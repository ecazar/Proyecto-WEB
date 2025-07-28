from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.fine import MultaCreate, MultaOut
from app.crud import fine as crud_fine
from app.db.session import SessionLocal

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=MultaOut)
async def crear_multa(multa: MultaCreate, db: AsyncSession = Depends(get_db)):
    return await crud_fine.create_multa(db, multa)

@router.get("/usuario/{usuario_id}", response_model=MultaOut)
async def obtener_multa_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    return await crud_fine.get_multa_por_usuario(db, usuario_id)