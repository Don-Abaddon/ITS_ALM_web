from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.users import User
from models.db import get_db
from schemas.users import UserOut
from typing import List

router = APIRouter()

@router.get("/users", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve a list of all users.
    """
    users = db.query(User).all()
    return users