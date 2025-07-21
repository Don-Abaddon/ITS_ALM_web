from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from models.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    ID = Column("id", Integer, primary_key=True, index=True)
    Nombre = Column("nombre", String, nullable=False)
    Usuario = Column("usuario", String, unique=True, nullable=False)
    Contrasena = Column("contrasena", String, nullable=False)
    Rol = Column("rol", String, nullable=False)
    Activo = Column("activo", Boolean, default=True)
    