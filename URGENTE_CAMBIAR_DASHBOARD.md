# 🚨 URGENTE: Cambiar Comando en Render Dashboard

## ⚠️ PROBLEMA ACTUAL

Render está ejecutando:
```
==> Running 'gunicorn app:app'  ❌
```

Pero debería ejecutar:
```
==> Running 'gunicorn metrolima_api.wsgi:application'  ✅
```

## ✅ SOLUCIÓN (5 MINUTOS)

### Paso 1: Ir al Dashboard de Render

1. Abre https://dashboard.render.com
2. Inicia sesión
3. Selecciona tu servicio **metrolima-api**

### Paso 2: Cambiar el Start Command

1. Haz clic en **"Settings"** (en el menú lateral izquierdo)
2. Busca la sección **"Build & Deploy"** o **"Start Command"**
3. Verás un campo que dice:
   ```
   Start Command: gunicorn app:app
   ```
4. **BORRA TODO** ese campo y déjalo **COMPLETAMENTE VACÍO**
5. O si no puedes dejarlo vacío, cámbialo a:
   ```
   gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT
   ```

### Paso 3: Guardar y Deploy

1. Haz clic en **"Save Changes"** (botón azul)
2. Render hará un nuevo deploy automáticamente
3. O haz clic en **"Manual Deploy"** → **"Deploy latest commit"**

### Paso 4: Verificar

1. Ve a **"Logs"** en tu servicio
2. Debe mostrar:
   ```
   ==> Running 'gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT'
   ```
3. **NO debe mostrar:**
   ```
   ==> Running 'gunicorn app:app'  ❌
   ```

## 📸 Ubicación Visual

```
Render Dashboard
  └── Tu Servicio (metrolima-api)
      └── Settings
          └── Build & Deploy
              └── Start Command  ← AQUÍ está el problema
```

## 🔍 Si No Encuentras el Campo

El campo puede estar en diferentes lugares según la versión de Render:

- **Settings** → **Build & Deploy** → **Start Command**
- **Settings** → **Environment** → **Start Command**
- **Settings** → **Advanced** → **Start Command**

Busca cualquier campo que diga "Start Command" o "Command to run".

## ⚠️ IMPORTANTE

**El Procfile y render.yaml están correctos en el repositorio**, pero Render está usando un comando manual del dashboard que tiene **prioridad más alta**.

**NO hay forma de solucionarlo desde el código.** Debes cambiarlo en el dashboard.

## ✅ Después de Cambiar

Una vez que cambies el comando en el dashboard, el deploy debería funcionar correctamente.

Si aún tienes problemas, verifica también:
- Variables de entorno (SECRET_KEY, ALLOWED_HOSTS, DEBUG)
- Revisa los logs para ver otros errores

