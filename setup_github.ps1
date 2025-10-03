# 🚀 Script para preparar y subir proyecto a GitHub

# Este script automatiza el proceso de subir tu proyecto a GitHub
# Ejecutar paso a paso después de instalar Git

Write-Host "🔧 Preparando proyecto para GitHub..." -ForegroundColor Green

# Verificar que Git está instalado
try {
    git --version
    Write-Host "✅ Git está instalado" -ForegroundColor Green
} catch {
    Write-Host "❌ Git no está instalado. Instálalo desde: https://git-scm.com/download/win" -ForegroundColor Red
    exit 1
}

# Configurar Git (cambiar estos valores)
Write-Host "⚙️ Configurando Git..." -ForegroundColor Yellow
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@example.com"

# Mostrar estructura del proyecto
Write-Host "📁 Estructura del proyecto:" -ForegroundColor Cyan
Get-ChildItem -Name | Where-Object { $_ -notlike ".*" -and $_ -ne "__pycache__" -and $_ -ne ".venv" }

# Inicializar repositorio
Write-Host "🚀 Inicializando repositorio Git..." -ForegroundColor Yellow
git init

# Agregar archivos
Write-Host "📦 Agregando archivos..." -ForegroundColor Yellow
git add .

# Mostrar estado
Write-Host "📋 Estado del repositorio:" -ForegroundColor Cyan
git status

# Hacer commit inicial
Write-Host "💾 Haciendo commit inicial..." -ForegroundColor Yellow
git commit -m "🎉 Initial commit: FastAPI project with CRUD, tests and docs

✨ Features:
- Complete CRUD API with FastAPI
- Automatic data validation with Pydantic
- Interactive documentation (Swagger UI)
- Automated tests with pytest
- Professional project structure
- Comprehensive documentation

🚀 Ready for production deployment"

# Instrucciones finales
Write-Host "`n🎯 PRÓXIMOS PASOS:" -ForegroundColor Green
Write-Host "1. Crear repositorio en GitHub:" -ForegroundColor White
Write-Host "   - Ve a https://github.com/new" -ForegroundColor Gray
Write-Host "   - Nombre: fastapi-project-template" -ForegroundColor Gray  
Write-Host "   - Descripción: API REST completa con FastAPI, tests y documentación" -ForegroundColor Gray
Write-Host "   - Visibilidad: Private 🔒" -ForegroundColor Gray
Write-Host "   - NO agregues README ni .gitignore (ya los tienes)" -ForegroundColor Gray

Write-Host "`n2. Conectar y subir:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/TU-USUARIO/fastapi-project-template.git" -ForegroundColor Gray
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray

Write-Host "`n3. Autenticación:" -ForegroundColor White  
Write-Host "   - Usa Personal Access Token como contraseña" -ForegroundColor Gray
Write-Host "   - O instala GitHub CLI: winget install GitHub.cli" -ForegroundColor Gray

Write-Host "`n✅ Proyecto preparado para GitHub!" -ForegroundColor Green