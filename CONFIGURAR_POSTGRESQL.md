# 🚀 SOLUCIÓN DEFINITIVA: Configurar PostgreSQL en Render

## ⚠️ Problema Actual

SQLite no persiste en Render porque el filesystem es **efímero**. Cada vez que se reinicia el servicio, la base de datos se pierde.

## ✅ Solución: PostgreSQL (5 minutos)

### Paso 1: Crear Base de Datos PostgreSQL en Render

1. Ve a https://dashboard.render.com
2. Click en **"New"** → **"PostgreSQL"**
3. Configura:
   - **Name:** `metrolima-db`
   - **Database:** `metrolima_db`
   - **User:** (se genera automáticamente)
   - **Region:** Elige la misma región que tu servicio web
4. Click en **"Create Database"**

### Paso 2: Conectar la Base de Datos al Servicio Web

1. Ve a tu servicio web **metrolima-api**
2. Ve a **Settings** → **Connections**
3. En **"Add Database"**, selecciona **metrolima-db**
4. Click en **"Connect"**

Render configurará automáticamente la variable de entorno `DATABASE_URL`.

### Paso 3: Verificar Variables de Entorno

1. Ve a **Settings** → **Environment**
2. Verifica que existe `DATABASE_URL` (Render la configura automáticamente)
3. Si no existe, agrégalo manualmente con el valor que Render te proporciona

### Paso 4: Hacer Deploy

1. Render detectará el cambio automáticamente
2. O haz **"Manual Deploy"** → **"Deploy latest commit"**

## ✅ ¡Listo!

Con PostgreSQL:
- ✅ La base de datos **persiste** entre reinicios
- ✅ Las migraciones se ejecutan una sola vez
- ✅ Funciona correctamente en producción
- ✅ No más errores de "no such table"

## 📝 Nota

El código ya está configurado para usar PostgreSQL automáticamente si existe `DATABASE_URL`. Solo necesitas crear la base de datos en Render.

