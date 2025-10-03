"""
Ejemplos prácticos para expandir tu API FastAPI
Este archivo muestra patrones comunes que puedes implementar
"""

from typing import List, Optional
from datetime import datetime
from enum import Enum
from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field, validator


# =============================================================================
# MODELOS AVANZADOS CON VALIDACIONES
# =============================================================================

class ItemStatus(str, Enum):
    """Enum para estados del item"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SOLD = "sold"


class ItemCreate(BaseModel):
    """Modelo para crear items (sin ID)"""
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del item")
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0, description="Precio debe ser mayor a 0")
    category: str = Field(..., min_length=1, max_length=50)
    status: ItemStatus = ItemStatus.ACTIVE
    
    @validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('El precio debe ser positivo')
        return round(v, 2)  # Redondear a 2 decimales


class ItemResponse(BaseModel):
    """Modelo para respuestas (con metadatos)"""
    id: int
    name: str
    description: Optional[str]
    price: float
    category: str
    status: ItemStatus
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True  # Para compatibilidad con SQLAlchemy


# =============================================================================
# PARÁMETROS DE CONSULTA AVANZADOS
# =============================================================================

class ItemFilters(BaseModel):
    """Filtros para buscar items"""
    category: Optional[str] = None
    status: Optional[ItemStatus] = None
    min_price: Optional[float] = Field(None, ge=0)
    max_price: Optional[float] = Field(None, ge=0)
    search: Optional[str] = Field(None, min_length=1)


# =============================================================================
# DEPENDENCIAS Y UTILIDADES
# =============================================================================

def get_pagination_params(
    skip: int = Query(0, ge=0, description="Elementos a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Límite de elementos")
):
    """Parámetros de paginación reutilizables"""
    return {"skip": skip, "limit": limit}


def validate_item_exists(item_id: int, db: dict):
    """Validar que un item existe en la 'base de datos'"""
    if item_id not in db:
        raise HTTPException(
            status_code=404, 
            detail=f"Item con ID {item_id} no encontrado"
        )
    return db[item_id]


# =============================================================================
# ENDPOINTS AVANZADOS (EJEMPLOS)
# =============================================================================

# Estos son ejemplos de endpoints que podrías agregar a tu API:

"""
@app.get("/items/search", response_model=List[ItemResponse])
async def search_items(
    filters: ItemFilters = Depends(),
    pagination: dict = Depends(get_pagination_params)
):
    # Implementar búsqueda con filtros
    # Aplicar paginación
    pass


@app.get("/items/categories", response_model=List[str])
async def get_categories():
    # Retornar lista única de categorías
    pass


@app.get("/items/stats")
async def get_stats():
    # Estadísticas: total items, promedio precios, etc.
    return {
        "total_items": len(_db),
        "average_price": sum(item.price for item in _db.values()) / len(_db) if _db else 0,
        "categories": len(set(item.category for item in _db.values())),
        "by_status": {
            status.value: sum(1 for item in _db.values() if item.status == status)
            for status in ItemStatus
        }
    }


@app.post("/items/bulk", response_model=List[ItemResponse])
async def create_bulk_items(items: List[ItemCreate]):
    # Crear múltiples items de una vez
    pass


@app.patch("/items/{item_id}/status")
async def update_item_status(item_id: int, status: ItemStatus):
    # Actualizar solo el estado de un item
    pass
"""


# =============================================================================
# MIDDLEWARE PERSONALIZADO
# =============================================================================

"""
from fastapi import Request
import time

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
"""


# =============================================================================
# MANEJO DE ERRORES PERSONALIZADO
# =============================================================================

"""
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": f"Error de validación: {str(exc)}"}
    )
"""


# =============================================================================
# CONFIGURACIÓN POR AMBIENTE
# =============================================================================

"""
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Mi API"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "your-secret-key"
    
    class Config:
        env_file = ".env"

settings = Settings()
"""


if __name__ == "__main__":
    print("Este archivo contiene ejemplos para expandir tu API.")
    print("Copia y adapta los patrones que necesites en proyecto_api.py")