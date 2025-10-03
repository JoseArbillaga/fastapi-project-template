# Guía Completa - Tu Primera API con FastAPI

## ✅ Lo que ya tienes funcionando

Tu API incluye:
- **CRUD completo** para Items (Create, Read, Update, Delete)
- **Documentación automática** en `/docs` (Swagger UI)
- **Validación de datos** con Pydantic
- **Manejo de errores** con códigos HTTP apropiados
- **Tests automatizados** con pytest
- **CORS habilitado** para desarrollo frontend

## 🚀 Cómo usar tu API

### Iniciar el servidor
```powershell
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Opción 1: Ejecutar directamente
python proyecto_api.py

# Opción 2: Con uvicorn (recomendado para desarrollo)
uvicorn proyecto_api:app --reload --host 127.0.0.1 --port 8000
```

### Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Mensaje de bienvenida |
| GET | `/docs` | Documentación interactiva |
| GET | `/items` | Listar todos los items |
| POST | `/items` | Crear un nuevo item |
| GET | `/items/{id}` | Obtener item por ID |
| PUT | `/items/{id}` | Actualizar item |
| DELETE | `/items/{id}` | Eliminar item |

### Ejemplos de uso con curl

```powershell
# Crear un item
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"name":"Laptop","description":"Gaming laptop","price":1200.50}'

# Listar items
curl "http://127.0.0.1:8000/items"

# Obtener item específico
curl "http://127.0.0.1:8000/items/1"

# Actualizar item
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Laptop Pro","description":"Updated gaming laptop","price":1400.00}'

# Eliminar item
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

## 🔧 Próximos pasos para expandir tu API

### 1. Base de datos real
Reemplaza el diccionario en memoria por SQLite o PostgreSQL:
```python
# Instalar: pip install sqlalchemy databases[sqlite]
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
```

### 2. Autenticación y autorización
```python
# Instalar: pip install python-jose[cryptography] passlib[bcrypt]
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
```

### 3. Variables de entorno
```python
# Instalar: pip install python-deque
from decouple import config
```

### 4. Logging y monitoreo
```python
import logging
from fastapi import Request
import time
```

### 5. Validaciones avanzadas
```python
from pydantic import validator, Field
from typing import Annotated
```

## 🧪 Ejecutar tests
```powershell
# Todos los tests
python -m pytest tests/ -v

# Tests específicos
python -m pytest tests/test_api.py::test_crud_item -v

# Con cobertura
pip install pytest-cov
python -m pytest tests/ --cov=proyecto_api --cov-report=html
```

## 📝 Conceptos clave aprendidos

### 1. **FastAPI** vs Flask
- **Ventajas**: Validación automática, documentación auto-generada, async nativo
- **Desempeño**: Más rápido que Flask para APIs
- **Desarrollo**: Menos código, más productivo

### 2. **Pydantic Models**
```python
class Item(BaseModel):
    name: str                    # Campo obligatorio
    price: float                 # Validación de tipo automática
    description: Optional[str]   # Campo opcional
```

### 3. **HTTP Status Codes**
- `200`: OK (GET exitoso)
- `201`: Created (POST exitoso)
- `204`: No Content (DELETE exitoso)
- `404`: Not Found
- `422`: Validation Error

### 4. **Async/Await**
```python
async def get_item():  # Función asíncrona
    # Útil para operaciones I/O (DB, APIs externas)
    pass
```

## 🌐 Despliegue en producción

### Heroku
```powershell
# Crear Procfile
echo "web: uvicorn proyecto_api:app --host=0.0.0.0 --port=${PORT:-5000}" > Procfile
```

### Docker
```dockerfile
FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "proyecto_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Railway/Vercel
Compatible directamente con FastAPI.

¡Ya tienes una base sólida para cualquier proyecto de API! 🎉