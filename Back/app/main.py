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

if __name__ == "__main__":
    import uvicorn
    # Run the app with uvicorn if this script is executed directly
    uvicorn.run(app, host="127.0.0.1", port=8000)  # Adjust host and port as needed
# Note: The host is set to "127.0.0.1" to allow access only from the local machine.
# If you want to run the app with a specific host, replace "127.0.0.1" with "0.0.0.0" to allow access from any IP address.
# This line is for running the app with uvicorn directly; remove if using a different server setup
# Note: The recommended way to run the app is from the command line using: uvicorn main:app --reload
# To run the app, use the command: uvicorn main:app --reload    
    