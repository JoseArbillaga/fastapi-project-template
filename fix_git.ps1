# 🔧 Script para solucionar problemas con Git

Write-Host "🔧 Solucionando problemas con Git..." -ForegroundColor Green

# Agregar Git al PATH de la sesión actual
$env:PATH += ";C:\Program Files\Git\bin"

# Verificar que Git funciona
try {
    $gitVersion = git --version
    Write-Host "✅ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git no se encuentra. Instalando..." -ForegroundColor Red
    
    # Intentar instalar con winget
    try {
        winget install --id Git.Git -e --source winget --force
        Write-Host "✅ Git instalado. Reinicia PowerShell y ejecuta este script nuevamente." -ForegroundColor Yellow
        pause
        exit
    } catch {
        Write-Host "❌ Error instalando Git. Descárgalo manualmente de: https://git-scm.com/download/win" -ForegroundColor Red
        Start-Process "https://git-scm.com/download/win"
        pause
        exit
    }
}

Write-Host ""
Write-Host "⚙️ Configurando Git..." -ForegroundColor Yellow

# Pedir datos al usuario
$userName = Read-Host "Ingresa tu nombre para Git (ejemplo: Jose Martinez)"
if ([string]::IsNullOrWhiteSpace($userName)) {
    $userName = "Jose"
}

$userEmail = Read-Host "Ingresa tu email para Git (ejemplo: jose@gmail.com)"
if ([string]::IsNullOrWhiteSpace($userEmail)) {
    $userEmail = "jose@example.com"
}

# Configurar Git
git config --global user.name "$userName"
git config --global user.email "$userEmail"

Write-Host "✅ Git configurado:" -ForegroundColor Green
Write-Host "   Nombre: $userName" -ForegroundColor Gray
Write-Host "   Email: $userEmail" -ForegroundColor Gray

Write-Host ""
Write-Host "🚀 Inicializando repositorio..." -ForegroundColor Yellow

# Inicializar repositorio
git init

# Agregar archivos
Write-Host "📦 Agregando archivos..." -ForegroundColor Yellow
git add .

# Mostrar estado
Write-Host "📋 Estado del repositorio:" -ForegroundColor Cyan
git status --short

# Hacer commit
Write-Host "💾 Creando commit inicial..." -ForegroundColor Yellow
git commit -m "🎉 Initial commit: FastAPI project with CRUD, tests and docs

✨ Features:
- Complete CRUD API with FastAPI
- Automatic data validation with Pydantic  
- Interactive documentation (Swagger UI)
- Automated tests with pytest
- Professional project structure
- Comprehensive documentation

🚀 Ready for GitHub!"

Write-Host ""
Write-Host "🎯 SIGUIENTE PASO - CREAR REPOSITORIO EN GITHUB:" -ForegroundColor Green
Write-Host "1. Ve a: https://github.com/new" -ForegroundColor White
Write-Host "2. Repository name: fastapi-project-template" -ForegroundColor Gray
Write-Host "3. Description: API REST completa con FastAPI" -ForegroundColor Gray
Write-Host "4. Visibilidad: Private 🔒" -ForegroundColor Gray
Write-Host "5. NO agregues README ni .gitignore" -ForegroundColor Gray

Write-Host ""
Write-Host "🔗 COMANDOS PARA CONECTAR CON GITHUB:" -ForegroundColor Green
Write-Host "git remote add origin https://github.com/TU-USUARIO/fastapi-project-template.git" -ForegroundColor Gray
Write-Host "git branch -M main" -ForegroundColor Gray
Write-Host "git push -u origin main" -ForegroundColor Gray

Write-Host ""
Write-Host "🔐 AUTENTICACIÓN:" -ForegroundColor Yellow
Write-Host "Cuando Git pida credenciales:" -ForegroundColor White
Write-Host "- Usuario: tu-usuario-github" -ForegroundColor Gray
Write-Host "- Contraseña: Personal Access Token (NO tu contraseña)" -ForegroundColor Gray
Write-Host "Crear token en: GitHub → Settings → Developer settings → Personal access tokens" -ForegroundColor Gray

Write-Host ""
Write-Host "✅ ¡Git configurado y proyecto listo para GitHub!" -ForegroundColor Green

pause