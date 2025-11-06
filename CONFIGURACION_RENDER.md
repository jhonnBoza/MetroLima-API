# ⚙️ Configuración Final para Render

## ✅ Todo Está Listo

Este proyecto está **100% configurado** para Render. Solo necesitas seguir estos pasos:

## 🚀 Pasos en Render Dashboard

### 1. Crear/Configurar el Servicio Web

1. Ve a https://dashboard.render.com
2. Si ya tienes un servicio, ve a **Settings**
3. Si no, crea uno nuevo: **New** → **Web Service**

### 2. Configuración Básica

**IMPORTANTE:** Deja estos campos **VACÍOS** para que Render use los archivos del repositorio:

- **Build Command:** (VACÍO)
- **Start Command:** (VACÍO)

Render usará automáticamente:
- `Procfile` para el Start Command
- `render.yaml` o ejecutará el build automáticamente

### 3. Variables de Entorno (OBLIGATORIAS)

Ve a **Settings** → **Environment** → **Environment Variables**

Agrega estas 3 variables:

```
SECRET_KEY=pm(x!4i!f=hcdy0@=e7@vihrli0&zags&uzkw=%-ybvk#8%7$9
ALLOWED_HOSTS=metrolima-api.onrender.com,*.onrender.com
DEBUG=False
```

**Nota:** Si quieres generar un nuevo SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Base de Datos (Opcional pero Recomendado)

1. Crea una base de datos PostgreSQL en Render
2. Conéctala a tu servicio web
3. Render configurará `DATABASE_URL` automáticamente

Si no usas PostgreSQL, Django usará SQLite (no recomendado para producción).

### 5. Deploy

- Si es un servicio nuevo, click en **"Create Web Service"**
- Si es existente, Render hará deploy automático o haz **"Manual Deploy"**

## 📋 Verificación Post-Deploy

### 1. Revisar Logs

Ve a **"Logs"** y verifica que diga:
```
==> Running 'gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT'
```

**NO debe decir:**
```
==> Running 'gunicorn app:app'  ❌
```

### 2. Probar la API

Tu API estará disponible en:
- URL: `https://metrolima-api.onrender.com`
- Endpoint: `https://metrolima-api.onrender.com/api/stations/`

Prueba con:
```bash
curl https://metrolima-api.onrender.com/api/stations/
```

O abre en el navegador:
```
https://metrolima-api.onrender.com/api/stations/
```

## 🔧 Si Algo Sale Mal

### Error 502 Bad Gateway

1. **Verifica Variables de Entorno:**
   - ¿Tienes `SECRET_KEY`?
   - ¿Tienes `ALLOWED_HOSTS`?
   - ¿Tienes `DEBUG=False`?

2. **Verifica Start Command:**
   - Debe estar **VACÍO** o decir: `gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT`

3. **Revisa los Logs:**
   - Ve a "Logs" y busca el error específico
   - Copia el error y busca la solución en `SOLUCION_502.md`

### Error: ModuleNotFoundError: No module named 'app'

- El Start Command está mal configurado
- Debe estar **VACÍO** o ser: `gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT`

### Error: DisallowedHost

- Agrega `ALLOWED_HOSTS=metrolima-api.onrender.com,*.onrender.com`

## 📁 Archivos del Repositorio

Todos estos archivos están en el repositorio y listos:

- ✅ `Procfile` - Comando de inicio
- ✅ `render.yaml` - Configuración de Infrastructure as Code
- ✅ `build.sh` - Script de build (opcional)
- ✅ `requirements.txt` - Dependencias
- ✅ `runtime.txt` - Versión de Python
- ✅ `metrolima_api/wsgi.py` - Aplicación WSGI

## ✅ Checklist Final

Antes de hacer deploy, verifica:

- [ ] Build Command está **VACÍO** en Render Dashboard
- [ ] Start Command está **VACÍO** en Render Dashboard
- [ ] `SECRET_KEY` está configurada
- [ ] `ALLOWED_HOSTS` está configurada
- [ ] `DEBUG=False` está configurada
- [ ] Base de datos PostgreSQL creada (opcional)
- [ ] Repositorio tiene todos los archivos necesarios

## 🎉 ¡Listo!

Con esta configuración, tu API debería funcionar perfectamente en Render.

Si tienes problemas, revisa:
- `SOLUCION_502.md` - Solución a errores comunes
- `README_RENDER.md` - Guía completa de despliegue
- Logs en Render Dashboard

