from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import Usuario
from app.schemas.user import UsuarioCreate

async def create_usuario(db: AsyncSession, usuario_data: UsuarioCreate):
    usuario = Usuario(
        login=usuario_data.login,
        # Quita esto: password=hashed_password,
        nombre=usuario_data.nombre,
        apellidos=usuario_data.apellidos,
        correo=usuario_data.correo,
        tipo=usuario_data.tipo,
        calle=usuario_data.calle,
        numero=usuario_data.numero,
        piso=usuario_data.piso,
        ciudad=usuario_data.ciudad,
        codigo_postal=usuario_data.codigo_postal,
        telefono_padres=usuario_data.telefono_padres,
        departamento=usuario_data.departamento
    )
    db.add(usuario)
    await db.commit()
    await db.refresh(usuario)
    return usuario
   

async def get_usuario_by_login(db: AsyncSession, login: str):
    result = await db.execute(select(Usuario).where(Usuario.login == login))
    return result.scalars().first()
