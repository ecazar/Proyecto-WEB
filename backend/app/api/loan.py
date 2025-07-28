from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.loan import PrestamoCreate, PrestamoOut, HistoricoPrestamoOut
from app.crud import loan as crud_loan
from app.db.session import SessionLocal
from app.core.deps import get_current_user
from typing import List
from datetime import date

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=PrestamoOut)
async def crear_prestamo(
    prestamo: PrestamoCreate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user)  # Protección por Keycloak
):
    return await crud_loan.create_prestamo(db, prestamo)

@router.get("/usuario/{usuario_id}", response_model=List[PrestamoOut])
async def prestamos_usuario(
    usuario_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user)
):
    return await crud_loan.get_prestamos_por_usuario(db, usuario_id)

@router.get("/historico/usuario/{usuario_id}", response_model=List[HistoricoPrestamoOut])
async def historico_prestamos(
    usuario_id: int, 
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user)
):
    return await crud_loan.get_historico_prestamos_usuario(db, usuario_id)

@router.post("/devolver/{prestamo_id}", response_model=HistoricoPrestamoOut)
async def devolver_prestamo(
    prestamo_id: int,
    fecha_devolucion: date,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user)
):
    historico = await crud_loan.devolver_prestamo(db, prestamo_id, fecha_devolucion)
    if historico is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return historico
