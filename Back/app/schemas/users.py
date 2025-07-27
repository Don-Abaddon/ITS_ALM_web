#schemas/users.py
from pydantic import BaseModel
from typing import Optional

class RolOut(BaseModel):
    idrol: int
    rol: str
    
    class Config:
        from_attributes = True
        
class UserOut(BaseModel):
    ID: int
    Name: str
    LastName: str
    Username: str
    Email: str
    Rol: RolOut
    Active: bool
    
    class Config:
        from_attributes = True

class UserIn(BaseModel):
    Name: str
    LastName: str
    Username: str
    Email: str
    Password: str
    RolID: int
    Active: Optional[bool] = True
    
    class Config:
        from_attributes = True

class PasswordUpdate(BaseModel):
    Password: str
    
    class Config:
        from_attributes = True