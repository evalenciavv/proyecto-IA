from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    estado: Optional[bool] = None

class UsuarioResponse(UsuarioBase):
    id: UUID
    estado: bool

    class Config:
        from_attributes = True
