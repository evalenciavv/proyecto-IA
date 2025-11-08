# models.py
from sqlalchemy import Column, String, Boolean, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "usuario"}  # Esquema PostgreSQL

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    contrasena = Column(String, nullable=False)
    estado = Column(Boolean, default=True)
    fecha_creacion = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    fecha_eliminacion = Column(TIMESTAMP(timezone=True))
