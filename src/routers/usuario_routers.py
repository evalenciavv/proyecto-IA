from fastapi import APIRouter, Depends, HTTPException
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import async_session
from src.model.usuario import Usuario
from src.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from uuid import UUID
import datetime

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Dependencia de DB
async def get_db():
    async with async_session() as session:
        yield session

# Listar usuarios activos
@router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Usuario).where(Usuario.estado == True))
    return result.scalars().all()

# Obtener usuario por ID
@router.get("/{usuario_id}", response_model=UsuarioResponse)
async def obtener_usuario(usuario_id: UUID, db: AsyncSession = Depends(get_db)):
    usuario = await db.get(Usuario, usuario_id)
    if not usuario or not usuario.estado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear nuevo usuario
@router.post("/", response_model=UsuarioResponse)
async def crear_usuario(usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    try:
        await db.commit()
        await db.refresh(nuevo_usuario)
    except IntegrityError as e:
        await db.rollback()
        if 'usuario_correo_key' in str(e.orig):
            raise HTTPException(status_code=400, detail="El correo ya está registrado.")
        raise HTTPException(status_code=400, detail="Error de integridad en los datos.")
    return nuevo_usuario


# Actualizar usuario
@router.put("/{usuario_id}", response_model=UsuarioResponse)
async def actualizar_usuario(usuario_id: UUID, datos: UsuarioUpdate, db: AsyncSession = Depends(get_db)):
    usuario = await db.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    for key, value in datos.model_dump(exclude_unset=True).items():
        setattr(usuario, key, value)

    usuario.fecha_actualizacion = datetime.datetime.now(datetime.timezone.utc)
    await db.commit()
    await db.refresh(usuario)
    return usuario

# Eliminar (lógico → estado = False)
@router.delete("/{usuario_id}")
async def eliminar_usuario(usuario_id: UUID, db: AsyncSession = Depends(get_db)):
    usuario = await db.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.estado = False
    usuario.fecha_eliminacion = datetime.datetime.now(datetime.timezone.utc)
    await db.commit()
    return {"message": f"Usuario {usuario_id} eliminado correctamente"}
