# 🚀 Inicio Rápido - API Django MetroLima

## 📋 Pasos para Iniciar el Servidor

### 1. Activar el Entorno Virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Crear Migraciones

```bash
python manage.py makemigrations
```

### 3. Aplicar Migraciones

```bash
python manage.py migrate
```

### 4. Crear Superusuario (opcional, para acceder al admin)

```bash
python manage.py createsuperuser
```

### 5. Ejecutar el Servidor

```bash
python manage.py runserver 0.0.0.0:8000
```

**Importante:** Usa `0.0.0.0:8000` para que sea accesible desde tu dispositivo Android en la misma red.

### 6. Acceder a la API

- **API de estaciones:** http://localhost:8000/api/stations/
- **Admin Django:** http://localhost:8000/admin/
- **Estaciones por línea:** http://localhost:8000/api/stations/by_line/?line=Línea 1

## 📱 Configurar Android

En `app/src/main/java/com/tecsup/metrolimago1/data/remote/StationApiService.kt`, cambia:

```kotlin
private const val DEFAULT_BASE_URL = "http://TU_IP_LOCAL:8000/api/"
```

**Para encontrar tu IP local:**
- Windows: `ipconfig` en CMD → busca "IPv4"
- Linux/Mac: `ifconfig` o `ip addr`

Ejemplo: `http://192.168.1.100:8000/api/`

## ✅ Próximos Pasos

1. Agregar estaciones desde el admin de Django
2. Probar la API desde el navegador
3. Configurar la URL en Android
4. Probar la sincronización desde la app

