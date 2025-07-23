# models/db.py
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_URL = f"sqlite:///{os.path.join(BASE_DIR, 'db', 'itsalm')}"


engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    print(f"Database URL: {DB_URL}")  # Debugging line to check the DB URL
    try:
        yield db
    finally:
        db.close()