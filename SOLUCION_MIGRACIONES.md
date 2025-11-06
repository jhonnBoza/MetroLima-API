# 🔧 Solución: Error "no such table: auth_user"

## ⚠️ Problema

El error `OperationalError: no such table: auth_user` significa que las migraciones de Django no se han ejecutado correctamente en Render.

## ✅ Solución

### Opción 1: Ejecutar Migraciones Manualmente (Rápido)

1. Ve a tu servicio en Render Dashboard
2. Abre la consola/terminal (si está disponible)
3. O crea un "Shell Command" temporal y ejecuta:
   ```bash
   python manage.py migrate
   ```

### Opción 2: Verificar Build Command en Render

1. Ve a **Settings** → **Build & Deploy**
2. Verifica que el **Build Command** incluya:
   ```
   pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput --clear
   ```
3. Si no está, agrégalo
4. Guarda y haz un nuevo deploy

### Opción 3: Usar el Script de Build

El archivo `build.sh` está configurado para ejecutar las migraciones automáticamente. Asegúrate de que Render lo use:

1. En **Settings** → **Build & Deploy** → **Build Command**
2. Usa:
   ```
   chmod +x build.sh && ./build.sh
   ```

### Opción 4: Ejecutar Migraciones en el Start Command (Temporal)

Como solución temporal, puedes agregar las migraciones al start command:

1. Ve a **Settings** → **Build & Deploy** → **Start Command**
2. Cambia a:
   ```
   python manage.py migrate --noinput && gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
   ```

**Nota:** Esto ejecutará las migraciones cada vez que se inicie el servicio, lo cual no es ideal pero funciona como solución temporal.

## 🔍 Verificación

Después de ejecutar las migraciones, verifica:

1. **Revisa los logs** en Render
2. Debe mostrar:
   ```
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions, stations
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     ...
   ```

3. **Prueba el admin:**
   - Ve a `https://metrolima-api.onrender.com/admin/`
   - Debe cargar sin el error de "no such table"

## 📝 Notas Importantes

- Las migraciones deben ejecutarse **durante el build**, no durante el start
- Si usas PostgreSQL, asegúrate de que `DATABASE_URL` esté configurada
- Si usas SQLite, el archivo `db.sqlite3` se creará automáticamente

## 🎯 Solución Recomendada

La mejor solución es asegurarse de que el **Build Command** en Render incluya:
```
python manage.py migrate --noinput
```

Y que se ejecute correctamente durante el build.

