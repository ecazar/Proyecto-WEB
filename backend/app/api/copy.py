from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.copy import EjemplarCreate, EjemplarOut
from app.crud import copy as crud_copy
from app.db.session import SessionLocal
from app.core.deps import get_current_user  # Protección con token

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=EjemplarOut)
async def crear_ejemplar(
    ejemplar: EjemplarCreate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user)  # Verificación de token
):
    return await crud_copy.create_ejemplar(db, ejemplar)