# ITS_ALM_web

Aplicación web para el manejo de usuarios y autenticación. Dividida en frontend y backend, con rutas protegidas, gestión de usuarios y diseño modular.

## 📁 Estructura del Proyecto

```
.
├── activar_env.sh                 # Script para activar entorno virtual
├── runserver.sh                  # Script para iniciar el servidor
├── .env                          # Variables de entorno (ignorado por Git)
├── Back/                         # Backend del proyecto (FastAPI)
│   ├── app/
│   │   ├── main.py               # Punto de entrada del backend
│   │   ├── models/               # Definición de modelos SQLAlchemy
│   │   ├── routes/               # Rutas de la API
│   │   ├── schemas/              # Pydantic schemas (Request/Response)
│   │   └── security/             # Manejo de hashing, autenticación
│   └── db/                       # Scripts y archivos de la base de datos
│       ├── create users table.sql
│       └── itsalm                # Archivo de base de datos SQLite
├── Front/                        # Interfaz web del proyecto
│   ├── index.html                # Página de login
│   ├── dash.html                 # Panel principal
│   ├── css/
│   │   └── style.css             # Estilos personalizados
│   ├── js/
│   │   └── conn.js               # Lógica JS para conectar al backend
│   └── pages/                    # Vistas futuras adicionales
```

## 🚀 Tecnologías utilizadas

- **Backend**: FastAPI, SQLAlchemy, Pydantic, SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticación**: JWT + `passlib` (hashing de contraseñas)

## 🛠️ Instrucciones básicas

```bash
# Crear entorno virtual
python3 -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r Back/app/requirements.txt

# Ejecutar backend
cd Back/app
uvicorn main:app --reload

# Ver aplicación
Abrir index.html desde carpeta Front/
```