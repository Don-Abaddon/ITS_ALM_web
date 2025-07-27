#routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from models.users import User
from models.db import get_db
from schemas.users import UserIn, UserOut, UserUpdate
from typing import List
from security.security import get_password_hash
from fastapi import status
router = APIRouter()

@router.get("/users", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve a list of all users.
    """
    if not db:
        raise HTTPException(status_code=404, detail="Database not found")
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
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """ Update an password user by ID.
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

@router.patch("/users/{user_id}", response_model=UserUpdate)
def update_user(user_id: int, patch_data: UserUpdate, db: Session = Depends(get_db)):
    """
    Update an existing user by ID.
    """
    db_user = db.query(User).filter(User.ID == user_id).first()
    cambios = {}
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if patch_data.Name is not None and patch_data.Name != db_user.Name:
        db_user.Name = patch_data.Name
        cambios["Name"] = patch_data.Name

    if patch_data.LastName is not None and patch_data.LastName != db_user.LastName:
        db_user.LastName = patch_data.LastName
        cambios["LastName"] = patch_data.LastName

    if patch_data.Email is not None and patch_data.Email != db_user.Email:
        db_user.Email = patch_data.Email
        cambios["Email"] = patch_data.Email
    
    db.commit()
    db.refresh(db_user)
    return db_user

@router.patch("/admin/users/{user_id}", response_model=UserUpdate)
def patch_admin_control(user_id: int, patch_data: UserUpdate, db: Session = Depends(get_db)):
    """
    Let admin update another user's Active and RolID.
    """
    db_user = db.query(User).filter(User.ID == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user.ID == user_id:
        raise HTTPException(status_code=403, detail="Cannot modify your own user")

    cambios = {}

    if patch_data.RolID is not None and patch_data.RolID != db_user.RolID:
        db_user.RolID = patch_data.RolID
        cambios["RolID"] = patch_data.RolID

    if patch_data.Active is not None and patch_data.Active != db_user.Active:
        db_user.Active = patch_data.Active
        cambios["Active"] = patch_data.Active

    if cambios:
        db.commit()
        db.refresh(db_user)

    return db_user
