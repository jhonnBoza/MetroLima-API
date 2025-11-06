# 🔧 Solución al Error 502 Bad Gateway

## ⚠️ Diagnóstico

El error **502 Bad Gateway** significa que Render no puede comunicarse con tu aplicación Django. Las causas más comunes son:

1. **Faltan variables de entorno** (SECRET_KEY, ALLOWED_HOSTS)
2. **No se ejecutaron las migraciones** de la base de datos
3. **El comando de inicio sigue siendo incorrecto** en el dashboard
4. **Problemas con la base de datos**

## ✅ Solución Paso a Paso

### Paso 1: Verificar el Comando de Inicio en Render Dashboard

1. Ve a https://dashboard.render.com
2. Selecciona tu servicio **metrolima-api**
3. Ve a **Settings** → **Build & Deploy**
4. Busca **"Start Command"**
5. Debe estar **VACÍO** o decir:
   ```
   gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT
   ```
6. Si dice `gunicorn app:app`, **cámbialo o déjalo vacío**
7. Guarda los cambios

### Paso 2: Configurar Variables de Entorno (OBLIGATORIO)

1. En el mismo servicio, ve a **Settings** → **Environment**
2. Busca **"Environment Variables"**
3. Agrega estas variables **OBLIGATORIAS**:

#### Variable 1: SECRET_KEY
```
Nombre: SECRET_KEY
Valor: [Genera uno nuevo - ver abajo]
```

**Generar SECRET_KEY:**
Ejecuta en tu terminal local:
```bash
cd c:/Users/Jhnn/Documents/MetroLimaGO/metrolima_api
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia el resultado y úsalo como valor de `SECRET_KEY`.

#### Variable 2: ALLOWED_HOSTS
```
Nombre: ALLOWED_HOSTS
Valor: metrolima-api.onrender.com,*.onrender.com
```

O para permitir todos (solo desarrollo):
```
Nombre: ALLOWED_HOSTS
Valor: *
```

#### Variable 3: DEBUG
```
Nombre: DEBUG
Valor: False
```

### Paso 3: Verificar Base de Datos

Si estás usando **PostgreSQL en Render**:
- Render debería configurar `DATABASE_URL` automáticamente
- Si no, crea una base de datos PostgreSQL en Render y conéctala a tu servicio

Si estás usando **SQLite** (no recomendado para producción):
- No necesitas configurar nada, Django lo usará por defecto
- **Nota:** SQLite puede causar problemas en producción

### Paso 4: Hacer un Nuevo Deploy

1. Después de configurar las variables, Render hará un deploy automático
2. O haz clic en **"Manual Deploy"** → **"Deploy latest commit"**

### Paso 5: Verificar los Logs

1. Ve a **"Logs"** en tu servicio
2. Busca errores relacionados con:
   - `SECRET_KEY`
   - `ALLOWED_HOSTS`
   - `migrate`
   - `ModuleNotFoundError`

## 🔍 Verificación Rápida

Después de configurar todo, los logs deberían mostrar:

```
==> Running build command...
==> Installing dependencies...
==> Running migrations...
==> Collecting static files...
==> Build successful 🎉
==> Deploying...
==> Running 'gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT'
```

Y NO debería aparecer:
```
==> Running 'gunicorn app:app'  ❌
```

## 📋 Checklist

- [ ] Start Command está vacío o es correcto
- [ ] SECRET_KEY está configurada
- [ ] ALLOWED_HOSTS está configurada
- [ ] DEBUG=False está configurada
- [ ] Se hizo un nuevo deploy
- [ ] Los logs no muestran errores

## 🆘 Si Sigue Fallando

1. **Revisa los logs completos** en Render
2. **Verifica que el repositorio tenga los archivos correctos:**
   - `Procfile` con el comando correcto
   - `render.yaml` actualizado
   - `requirements.txt` completo
3. **Prueba localmente:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   gunicorn metrolima_api.wsgi:application
   ```

## 📞 Recursos

- [Documentación de Render sobre 502](https://render.com/docs/troubleshooting-deploys)
- [Variables de entorno en Render](https://render.com/docs/environment-variables)

