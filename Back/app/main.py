# main.py
# This file is part of the ITS ALM project.
from fastapi import FastAPI
from routes import users
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()
# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; adjust in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Welcome to the ITS ALM API"}
app.include_router(users.router)