#!/bin/bash

# Navegar al folder base para FastAPI
cd ~/Desktop/D/ITS_ALM_web/Back/app

# Ejecutar el servidor
uvicorn main:app --reload
