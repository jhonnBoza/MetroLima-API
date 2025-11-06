# 🚨 INSTRUCCIONES URGENTES: Corregir Comando en Render Dashboard

## ⚠️ Problema

Render está ejecutando `gunicorn app:app` en lugar de usar el `Procfile` o `render.yaml`. Esto significa que hay un **comando manual configurado en el dashboard** que tiene prioridad.

## ✅ Solución: Cambiar el Comando en el Dashboard

### Pasos:

1. **Ve al Dashboard de Render:**
   - Accede a https://dashboard.render.com
   - Inicia sesión con tu cuenta

2. **Selecciona tu servicio web:**
   - Busca el servicio llamado "metrolima-api" o similar
   - Haz clic en él

3. **Ve a la sección "Settings":**
   - En el menú lateral, haz clic en **"Settings"**

4. **Busca "Start Command":**
   - Desplázate hasta la sección **"Build & Deploy"** o **"Start Command"**
   - Verás un campo que dice algo como:
     ```
     gunicorn app:app
     ```

5. **Cambia el comando:**
   - **OPCIÓN 1 (Recomendada):** Deja el campo **VACÍO** para que Render use automáticamente el `Procfile`
   - **OPCIÓN 2:** Cambia el comando a:
     ```
     gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT
     ```

6. **Guarda los cambios:**
   - Haz clic en **"Save Changes"** o el botón de guardar

7. **Haz un nuevo deploy:**
   - Render debería detectar el cambio automáticamente
   - O haz clic en **"Manual Deploy"** → **"Deploy latest commit"**

## 📸 Ubicación Visual

El campo "Start Command" generalmente se encuentra en:
```
Settings → Build & Deploy → Start Command
```

O en algunas versiones:
```
Settings → Environment → Start Command
```

## ✅ Verificación

Después de cambiar el comando, en los logs de Render deberías ver:
```
==> Running 'gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT'
```

En lugar de:
```
==> Running 'gunicorn app:app'
```

## 🔍 Si No Encuentras el Campo

Si no ves el campo "Start Command", puede estar en:
- **Environment Variables** (Variables de Entorno)
- **Advanced Settings** (Configuración Avanzada)
- O el servicio puede estar usando **Infrastructure as Code** (render.yaml)

En ese caso, el `render.yaml` que ya está en el repositorio debería funcionar, pero puede que necesites:
1. Eliminar el servicio actual
2. Crear uno nuevo usando "Infrastructure as Code" desde el `render.yaml`

## 📝 Nota Importante

**El `Procfile` y `render.yaml` están correctos en el repositorio**, pero Render está usando un comando manual del dashboard que tiene **prioridad más alta**. Por eso necesitas cambiarlo manualmente en el dashboard.

