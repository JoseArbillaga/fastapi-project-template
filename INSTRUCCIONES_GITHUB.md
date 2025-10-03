# 📋 Guía para subir tu proyecto a GitHub

## 🔧 Paso 1: Instalar Git (si no lo tienes)

### Opción A: Instalar Git desde el sitio oficial
1. Ve a https://git-scm.com/download/win
2. Descarga e instala Git para Windows
3. Durante la instalación, acepta las opciones por defecto

### Opción B: Instalar con Chocolatey (si lo tienes)
```powershell
choco install git
```

### Opción C: Instalar con winget
```powershell
winget install --id Git.Git -e --source winget
```

## ⚙️ Paso 2: Configurar Git (primera vez)

✅ **YA COMPLETADO** - Tu Git está configurado con:
- Nombre: Jarbillaga  
- Email: jarbillaga@gmail.com

```bash
# Solo si necesitas cambiar la configuración:
git config --global user.name "Jarbillaga"
git config --global user.email "jarbillaga@gmail.com"
```

## 🚀 Paso 3: Crear repositorio en GitHub

1. Ve a https://github.com
2. Haz clic en el botón verde "New" o "+"
3. Completa el formulario:
   - **Repository name**: `fastapi-project-template` (o el nombre que prefieras)
   - **Description**: `API REST completa con FastAPI, tests y documentación`
   - **Visibility**: Selecciona "Private" 🔒
   - **NO** marques "Add a README file" (ya tienes uno)
   - **NO** marques "Add .gitignore" (ya tienes uno)
   - **Sí** puedes agregar una licencia si quieres

## 📁 Paso 4: Preparar y subir el proyecto

✅ **YA COMPLETADO** - Tu repositorio local está listo con:
- Repositorio inicializado
- Todos los archivos agregados  
- Commit inicial creado
- Rama cambiada a 'main'

**PRÓXIMO PASO:** Conectar con GitHub

```bash
# 4. Agregar el repositorio remoto (reemplaza TU-USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU-USUARIO/fastapi-project-template.git

# 5. Subir al repositorio (esto pedirá tu autenticación)
git push -u origin main
```

## 🔐 Paso 5: Autenticación en GitHub

GitHub ya no acepta contraseñas. Necesitas usar:

### Opción A: Personal Access Token (Recomendado)
1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Selecciona scopes: `repo` (full control)
4. Copia el token generado
5. Úsalo como contraseña cuando Git te la pida

### Opción B: GitHub CLI (Más fácil)
```bash
# Instalar GitHub CLI
winget install --id GitHub.cli

# Autenticarse
gh auth login
```

## 📋 Lista de verificación final

Antes de subir, verifica que tienes:

✅ `.gitignore` - Para excluir archivos innecesarios  
✅ `README.md` - Documentación principal actualizada  
✅ `LICENSE` - Licencia del proyecto  
✅ `requirements.txt` - Dependencias listadas  
✅ Tests funcionando - `pytest tests/ -v`  
✅ Código limpio - Sin archivos temporales  

## 🎯 Comandos útiles para el futuro

```bash
# Ver estado del repositorio
git status

# Agregar cambios específicos
git add archivo.py

# Agregar todos los cambios
git add .

# Hacer commit con mensaje descriptivo
git commit -m "✨ Add new feature: user authentication"

# Subir cambios
git push

# Ver historial
git log --oneline

# Crear nueva rama
git checkout -b feature/nueva-funcionalidad

# Cambiar entre ramas
git checkout main
git checkout feature/nueva-funcionalidad

# Fusionar rama
git checkout main
git merge feature/nueva-funcionalidad
```

## 🏷️ Convenciones de commits recomendadas

Usa estos prefijos para tus mensajes de commit:

- `🎉 Initial commit` - Primer commit
- `✨ feat:` - Nueva funcionalidad
- `🐛 fix:` - Corrección de bugs
- `📚 docs:` - Documentación
- `💄 style:` - Cambios de formato/estilo
- `♻️ refactor:` - Refactorización de código
- `🧪 test:` - Agregar/modificar tests
- `📦 chore:` - Tareas de mantenimiento

Ejemplo: `✨ feat: add user authentication endpoints`

## 🔧 Configuración adicional recomendada

### Archivo .gitattributes (opcional)
```
* text=auto
*.py text eol=lf
*.md text eol=lf
*.yml text eol=lf
*.yaml text eol=lf
```

### Template para Pull Requests
Crea `.github/pull_request_template.md`:
```markdown
## Descripción
Breve descripción de los cambios

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Breaking change
- [ ] Documentación

## Tests
- [ ] Tests pasan localmente
- [ ] Agregué nuevos tests si es necesario

## Checklist
- [ ] Mi código sigue las convenciones del proyecto
- [ ] He revisado mi propio código
- [ ] He actualizado la documentación si es necesario
```

---

Una vez que tengas Git instalado, ejecuta los comandos del **Paso 4** y tu proyecto estará en GitHub de forma profesional! 🚀