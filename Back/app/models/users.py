#models/users.py
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from models.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    ID = Column("iduser", Integer, primary_key=True, index=True)
    Name = Column("name", String, nullable=False)
    LastName = Column("lastname", String, nullable=False)
    Email = Column("email", String, unique=True, nullable=False)
    Username = Column("username", String, unique=True, nullable=False)
    Password = Column("password", String, nullable=False)
    RolID = Column("rol", Integer, ForeignKey('rol.idrol'))
    Active = Column("active", Boolean, default=True)

    Rol = relationship("Rol", lazy='joined', back_populates="user")

class Rol(Base):
    __tablename__ = "rol"
    
    idrol = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String, nullable=False)

    user = relationship("User", back_populates="Rol")

    
    