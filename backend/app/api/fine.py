from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
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
