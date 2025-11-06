# 🚨 INSTRUCCIONES URGENTES: Ejecutar Migraciones en Render

## ⚠️ Problema Actual

El error `no such table: auth_user` persiste porque las migraciones no se están ejecutando correctamente.

## ✅ Solución Inmediata

### Opción 1: Verificar Start Command en Render Dashboard (MÁS IMPORTANTE)

1. **Ve a Render Dashboard:**
   - https://dashboard.render.com
   - Selecciona tu servicio **metrolima-api**

2. **Ve a Settings → Build & Deploy:**
   - Busca el campo **"Start Command"**

3. **Verifica que diga EXACTAMENTE:**
   ```
   python manage.py migrate --noinput && gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
   ```

4. **Si NO dice eso:**
   - Bórralo completamente
   - O cámbialo al comando de arriba
   - **GUARDA los cambios**

5. **Haz un nuevo deploy:**
   - Click en "Manual Deploy" → "Deploy latest commit"

### Opción 2: Ejecutar Migraciones Manualmente (Solución Temporal)

Si el Start Command ya está correcto pero aún falla:

1. En Render Dashboard, busca una opción de **"Shell"** o **"Console"**
2. O crea un **"One-off Command"** temporal
3. Ejecuta:
   ```bash
   python manage.py migrate
   ```

### Opción 3: Verificar Build Command

1. Ve a **Settings → Build & Deploy**
2. Verifica que el **Build Command** incluya:
   ```
   pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput --clear
   ```

## 🔍 Verificación

Después de cambiar el Start Command y hacer deploy, en los **Logs** deberías ver:

```
📦 Ejecutando migraciones...
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, stations
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying stations.0001_initial... OK
🚀 Iniciando servidor...
```

## ⚠️ IMPORTANTE

**El problema más común es que Render está usando un Start Command diferente al del `render.yaml`.**

**Render Dashboard tiene prioridad sobre `render.yaml`**, así que **DEBES verificar y cambiar el Start Command en el dashboard manualmente**.

## 📋 Checklist

- [ ] Start Command en Render Dashboard es correcto
- [ ] Build Command incluye `python manage.py migrate --noinput`
- [ ] Se hizo un nuevo deploy después de cambiar
- [ ] Los logs muestran que las migraciones se ejecutaron
- [ ] El admin funciona sin el error "no such table: auth_user"

## 🆘 Si Nada Funciona

1. **Revisa los logs completos** en Render
2. **Busca errores relacionados con:**
   - `migrate`
   - `db.sqlite3`
   - `DATABASE_URL`
3. **Verifica que la base de datos SQLite tenga permisos de escritura**

