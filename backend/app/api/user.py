from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UsuarioCreate, UsuarioOut
from app.crud import user as crud_user
from app.db.session import SessionLocal
from app.core.deps import get_current_user

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=UsuarioOut)
async def crear_usuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user)  # Protección por Keycloak
):
    db_usuario = await crud_user.get_usuario_by_login(db, usuario.login)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Login ya registrado")
    return await crud_user.create_usuario(db, usuario)
