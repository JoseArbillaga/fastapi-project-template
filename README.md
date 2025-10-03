# 🚀 FastAPI Project Template

Una API REST completa construida con FastAPI, incluyendo validación de datos, documentación automática y tests.

## ✨ Características

- **FastAPI** - Framework moderno y rápido para APIs
- **Pydantic** - Validación automática de datos con type hints
- **Documentación automática** - Swagger UI y ReDoc integrados
- **Tests automatizados** - Suite completa con pytest
- **CORS habilitado** - Listo para desarrollo frontend
- **Código limpio** - Type hints, docstrings y buenas prácticas

## 🛠️ Instalación

### Prerrequisitos
- Python 3.9+
- pip

### Setup local

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repo>
   cd proyecto-api
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   ```

3. **Activar entorno virtual**
   ```bash
   # Windows
   .\.venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source .venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Uso

### Ejecutar el servidor

```bash
# Opción 1: Ejecutar directamente
python proyecto_api.py

# Opción 2: Con uvicorn (recomendado)
uvicorn proyecto_api:app --reload --host 127.0.0.1 --port 8000
```

La API estará disponible en: http://127.0.0.1:8000

### Documentación interactiva

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📚 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Mensaje de bienvenida |
| GET | `/items` | Listar todos los items |
| POST | `/items` | Crear un nuevo item |
| GET | `/items/{id}` | Obtener item por ID |
| PUT | `/items/{id}` | Actualizar item completo |
| DELETE | `/items/{id}` | Eliminar item |

## 🧪 Testing

```bash
# Ejecutar todos los tests
python -m pytest tests/ -v

# Ejecutar tests con cobertura
pip install pytest-cov
python -m pytest tests/ --cov=proyecto_api --cov-report=html

# Pruebas manuales
python test_manual.py
```

## 📖 Ejemplo de uso

```python
import requests

# Crear un item
response = requests.post("http://127.0.0.1:8000/items", json={
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1299.99
})

print(response.json())
# {'id': 1, 'name': 'Laptop', 'description': 'Gaming laptop', 'price': 1299.99}
```

## 🏗️ Estructura del proyecto

```
proyecto-api/
├── proyecto_api.py          # API principal
├── requirements.txt         # Dependencias
├── .gitignore              # Archivos ignorados por Git
├── tests/
│   └── test_api.py         # Tests automatizados
├── docs/
│   ├── GUIA_COMPLETA.md    # Documentación detallada
│   ├── ejemplos_avanzados.py # Patrones avanzados
│   └── PROYECTO_COMPLETADO.md # Resumen del proyecto
└── test_manual.py          # Script de pruebas manuales
```

## 🔧 Tecnologías utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno
- **[Pydantic](https://docs.pydantic.dev/)** - Validación de datos
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[pytest](https://docs.pytest.org/)** - Framework de testing

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**JoseArbillaga** - **josearbillaga@gmail.com**

