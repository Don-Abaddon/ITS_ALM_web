#routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from models.users import User
from models.db import get_db
from schemas.users import UserOut, UserIn
from typing import List

router = APIRouter()

@router.get("/users", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve a list of all users.
    """
    users = db.query(User).all()
    return users

@router.post("/users", response_model=UserIn)
def create_user(user: UserIn, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    db_user = User(
        Name=user.Name,
        LastName=user.LastName,
        Username=user.Username,
        Email=user.Email,
        Password=user.Password,  # Ensure to hash the password in production
        RolID=user.RolID,
        Active=user.Active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user