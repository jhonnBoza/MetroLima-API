# 🚀 Guía de Despliegue en Render

## ✅ Configuración Completa para Render

Este proyecto está **completamente configurado** para desplegarse en Render sin conflictos.

## 📋 Archivos de Configuración

### 1. `Procfile`
Contiene el comando de inicio correcto:
```
web: gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT
```

### 2. `render.yaml`
Configuración completa de Infrastructure as Code para Render.

### 3. `build.sh`
Script que ejecuta migraciones y recopila archivos estáticos.

### 4. `requirements.txt`
Todas las dependencias necesarias.

## 🔧 Pasos para Desplegar

### Opción A: Usando el Dashboard de Render (Recomendado)

1. **Crear Nuevo Servicio Web:**
   - Ve a https://dashboard.render.com
   - Click en "New" → "Web Service"
   - Conecta tu repositorio: `https://github.com/jhonnBoza/MetroLima-API`
   - Selecciona la rama `main`

2. **Configuración Básica:**
   - **Name:** `metrolima-api`
   - **Environment:** `Python 3`
   - **Build Command:** (DÉJALO VACÍO - Render usará el render.yaml o ejecutará automáticamente)
   - **Start Command:** (DÉJALO VACÍO - Render usará el Procfile)

3. **Variables de Entorno (OBLIGATORIAS):**
   Ve a "Environment" y agrega:
   
   ```
   SECRET_KEY=pm(x!4i!f=hcdy0@=e7@vihrli0&zags&uzkw=%-ybvk#8%7$9
   ALLOWED_HOSTS=metrolima-api.onrender.com,*.onrender.com
   DEBUG=False
   DJANGO_SETTINGS_MODULE=metrolima_api.settings
   ```

4. **Base de Datos (Opcional pero Recomendado):**
   - Crea una base de datos PostgreSQL en Render
   - Conéctala a tu servicio web
   - Render configurará `DATABASE_URL` automáticamente

5. **Deploy:**
   - Click en "Create Web Service"
   - Render hará el deploy automáticamente

### Opción B: Usando Infrastructure as Code (render.yaml)

1. **Crear Servicio desde render.yaml:**
   - Ve a https://dashboard.render.com
   - Click en "New" → "Blueprint"
   - Conecta tu repositorio
   - Render detectará el `render.yaml` automáticamente

2. **Variables de Entorno:**
   Aún necesitas agregar manualmente:
   ```
   SECRET_KEY=pm(x!4i!f=hcdy0@=e7@vihrli0&zags&uzkw=%-ybvk#8%7$9
   ALLOWED_HOSTS=metrolima-api.onrender.com,*.onrender.com
   DEBUG=False
   ```

## ⚙️ Configuración del Dashboard

### Start Command
**IMPORTANTE:** Debe estar **VACÍO** para que Render use el `Procfile` automáticamente.

Si Render no detecta el Procfile, usa:
```
gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT
```

### Build Command
**IMPORTANTE:** Debe estar **VACÍO** para que Render use el comando del `render.yaml` o ejecute automáticamente:
```
pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput --clear
```

## 🔍 Verificación Post-Deploy

Después del deploy, verifica:

1. **Logs:**
   - Ve a "Logs" en tu servicio
   - Debe mostrar: `==> Running 'gunicorn metrolima_api.wsgi:application'`
   - NO debe mostrar: `==> Running 'gunicorn app:app'`

2. **URL del Servicio:**
   - Tu API estará disponible en: `https://metrolima-api.onrender.com`
   - Endpoint de estaciones: `https://metrolima-api.onrender.com/api/stations/`

3. **Prueba la API:**
   ```bash
   curl https://metrolima-api.onrender.com/api/stations/
   ```

## 🐛 Troubleshooting

### Error 502 Bad Gateway
- Verifica que `SECRET_KEY` y `ALLOWED_HOSTS` estén configuradas
- Revisa los logs para ver el error específico
- Asegúrate de que el Start Command esté vacío o sea correcto

### Error: ModuleNotFoundError: No module named 'app'
- El Start Command está incorrecto
- Debe estar vacío o decir: `gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT`

### Error: DisallowedHost
- Agrega `ALLOWED_HOSTS=metrolima-api.onrender.com,*.onrender.com`

### Error: SECRET_KEY must not be empty
- Agrega la variable `SECRET_KEY` en Environment Variables

## 📝 Notas Importantes

- **NUNCA** subas archivos `.env` al repositorio
- **SIEMPRE** usa `DEBUG=False` en producción
- **CONFIGURA** `ALLOWED_HOSTS` correctamente para seguridad
- El `Procfile` y `render.yaml` están en la raíz del proyecto
- Las migraciones se ejecutan automáticamente durante el build

## ✅ Checklist Pre-Deploy

- [ ] Repositorio tiene `Procfile` en la raíz
- [ ] Repositorio tiene `render.yaml` en la raíz
- [ ] Repositorio tiene `requirements.txt` en la raíz
- [ ] Variables de entorno configuradas en Render
- [ ] Start Command está vacío o es correcto
- [ ] Build Command está vacío o es correcto
- [ ] Base de datos PostgreSQL creada (opcional pero recomendado)

## 🎉 ¡Listo!

Con esta configuración, tu API debería desplegarse sin problemas en Render.

