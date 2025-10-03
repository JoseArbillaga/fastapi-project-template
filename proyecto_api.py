from typing import Dict, List, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: aquí se podría abrir conexión a bases de datos, configurar caches, etc.
    print("Iniciando aplicación...")
    yield
    # Shutdown: cerrar conexiones, limpiar recursos
    print("Cerrando aplicación...")


app = FastAPI(
    title="Proyecto API",
    version="0.1.0",
    description="API de ejemplo creada con FastAPI. Incluye modelos Pydantic, manejo básico de errores y documentación automática (OpenAPI).",
    lifespan=lifespan
)

# CORS: en desarrollo permitimos todo, en producción restringe los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


# Simulamos una 'base de datos' en memoria para ejemplos y pruebas
_db: Dict[int, Item] = {}
_next_id = 1


@app.get("/", tags=["Root"])
async def read_root():
    """Ruta raíz: devuelve un saludo y la ruta a la documentación."""
    return {"message": "Bienvenido a la API creada con FastAPI", "docs": "/docs"}


@app.get("/items", response_model=List[Item], tags=["Items"])
async def list_items():
    """Listar todos los items almacenados (simulación)."""
    return list(_db.values())


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
async def create_item(item: Item):
    """Crear un item nuevo. El id se asigna automáticamente."""
    global _next_id
    item.id = _next_id
    _db[_next_id] = item
    _next_id += 1
    return item


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
async def get_item(item_id: int):
    """Obtener un item por id. Devuelve 404 si no existe."""
    item = _db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item


@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
async def update_item(item_id: int, item: Item):
    """Actualizar un item existente por id."""
    stored = _db.get(item_id)
    if not stored:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    item.id = item_id
    _db[item_id] = item
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
async def delete_item(item_id: int):
    """Eliminar un item por id."""
    if item_id in _db:
        del _db[item_id]
        return
    raise HTTPException(status_code=404, detail="Item no encontrado")


if __name__ == "__main__":
    # Ejecutar con: python proyecto_api.py -> esto arranca uvicorn de forma embebida
    import uvicorn

    uvicorn.run("proyecto_api:app", host="127.0.0.1", port=8000, reload=True) 
