from pydantic import BaseModel
from typing import Optional


class UserOut(BaseModel):
    ID: int
    Nombre: str
    Usuario: str
    Rol: str
    Activo: bool
    
    class Config:
        from_attributes = True