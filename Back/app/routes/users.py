#routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from models.users import User
from models.db import get_db
from schemas.users import UserIn, UserOut, PasswordUpdate
from typing import List
from security.security import get_password_hash
from fastapi import status
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
        Password=get_password_hash(user.Password),  # Ensure to hash the password in production
        RolID=user.RolID,
        Active=user.Active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.patch("/users/{user_id}/password", status_code=204)
def update_user(user_id: int, user: PasswordUpdate, db: Session = Depends(get_db)):
    """ Update an existing user by ID.
    """
    db_user = db.query(User).filter(User.ID == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.Password = get_password_hash(user.Password)
    db.commit()
    return

@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):  
    """
    Retrieve a user by ID.
    """
    user = db.query(User).options(joinedload(User.Rol)).filter(User.ID == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user