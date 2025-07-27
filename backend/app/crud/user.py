# app/crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import Usuario, Alumno, Profesor
from app.schemas.user import UsuarioCreate
from app.schemas.common import EstadoUsuarioEnum

async def get_usuario_by_login(db: AsyncSession, login: str):
    result = await db.execute(select(Usuario).where(Usuario.login == login))
    return result.scalars().first()

async def create_usuario(db: AsyncSession, user_data: UsuarioCreate):
    nuevo_usuario = Usuario(
        tipo=user_data.tipo,
        login=user_data.login,
        password=user_data.password,  # Ideal: hashearlo con passlib
        nombre=user_data.nombre,
        apellidos=user_data.apellidos,
        correo=user_data.correo,
        estado=EstadoUsuarioEnum.activo,
        calle=user_data.direccion.calle,
        numero=user_data.direccion.numero,
        piso=user_data.direccion.piso,
        ciudad=user_data.direccion.ciudad,
        codigo_postal=user_data.direccion.codigo_postal
    )
    db.add(nuevo_usuario)
    await db.flush()  # Obtener el ID

    if user_data.tipo == "alumno":
        alumno = Alumno(id=nuevo_usuario.id)
        db.add(alumno)
    elif user_data.tipo == "profesor":
        profesor = Profesor(id=nuevo_usuario.id)
        db.add(profesor)

    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario
