# FastAPI Project Template

Una API REST profesional construida con FastAPI

## Descripción
Este proyecto es un template completo para crear APIs REST con FastAPI, incluyendo validación de datos, documentación automática, tests y mejores prácticas de desarrollo.

## Tecnologías
- FastAPI
- Pydantic 
- pytest
- Uvicorn

## Características
- CRUD completo
- Documentación automática (Swagger)
- Tests automatizados
- Validación de datos
- Manejo de errores
- CORS habilitado

## Setup
1. Clonar repositorio
2. Crear entorno virtual: `python -m venv .venv`
3. Activar entorno: `.\.venv\Scripts\Activate.ps1` 
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar: `python proyecto_api.py`

## Endpoints
- GET / - Bienvenida
- GET /items - Listar items
- POST /items - Crear item
- GET /items/{id} - Obtener item
- PUT /items/{id} - Actualizar item  
- DELETE /items/{id} - Eliminar item

## Tests
`python -m pytest tests/ -v`

## Documentación
http://127.0.0.1:8000/docs