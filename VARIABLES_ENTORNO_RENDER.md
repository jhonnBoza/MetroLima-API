# 🔐 Variables de Entorno Necesarias en Render

## ⚠️ Problema: Error 502 Bad Gateway

El error 502 generalmente ocurre porque:
1. Faltan variables de entorno necesarias
2. No se han ejecutado las migraciones de la base de datos
3. El servicio no puede conectarse a la base de datos

## ✅ Variables de Entorno Requeridas

Ve a tu servicio en Render Dashboard → **Settings** → **Environment Variables** y agrega:

### 1. SECRET_KEY (OBLIGATORIA)
```
SECRET_KEY=tu-clave-secreta-muy-larga-y-aleatoria-aqui
```

**Cómo generar una:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

O usa este comando en tu terminal local:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. DEBUG (Recomendada)
```
DEBUG=False
```

### 3. ALLOWED_HOSTS (OBLIGATORIA para producción)
```
ALLOWED_HOSTS=metrolima-api.onrender.com,*.onrender.com
```

O si quieres permitir todos (solo para desarrollo):
```
ALLOWED_HOSTS=*
```

### 4. DATABASE_URL (Si usas PostgreSQL en Render)
Si creaste una base de datos PostgreSQL en Render, Render la configura automáticamente. Pero si no, agrega:
```
DATABASE_URL=postgresql://usuario:password@host:puerto/database
```

**Nota:** Si no tienes PostgreSQL, Django usará SQLite por defecto (no recomendado para producción).

### 5. CORS_ALLOW_ALL_ORIGINS (Opcional)
```
CORS_ALLOW_ALL_ORIGINS=True
```

O para ser más específico:
```
CORS_ALLOWED_ORIGINS=https://tu-dominio.com,https://otro-dominio.com
```

## 📝 Pasos para Configurar

1. **Ve a Render Dashboard:**
   - https://dashboard.render.com
   - Selecciona tu servicio web

2. **Ve a Settings → Environment:**
   - Busca la sección "Environment Variables"

3. **Agrega cada variable:**
   - Haz clic en "Add Environment Variable"
   - Ingresa el nombre (ej: `SECRET_KEY`)
   - Ingresa el valor
   - Guarda

4. **Variables Mínimas Necesarias:**
   - `SECRET_KEY` (OBLIGATORIA)
   - `ALLOWED_HOSTS` (OBLIGATORIA)
   - `DEBUG=False` (Recomendada)

5. **Guarda y redeploy:**
   - Render hará un nuevo deploy automáticamente

## 🔍 Verificar Logs

Después de configurar las variables, revisa los logs en Render:
- Ve a "Logs" en tu servicio
- Busca errores relacionados con:
  - `SECRET_KEY`
  - `ALLOWED_HOSTS`
  - `DATABASE_URL`
  - Migraciones

## ⚠️ Importante

- **NUNCA** compartas tu `SECRET_KEY` públicamente
- **NUNCA** subas archivos `.env` al repositorio
- Usa `DEBUG=False` en producción
- Configura `ALLOWED_HOSTS` correctamente para seguridad

