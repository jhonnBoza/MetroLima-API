# MetroLima API

API REST para la aplicación MetroLima GO desarrollada con Django REST Framework.

## 🚀 Características

- API REST para estaciones del Metro de Lima
- Soporte CORS para aplicaciones móviles
- Base de datos SQLite (desarrollo) / PostgreSQL (producción)
- Despliegue en Render

## 📋 Requisitos

- Python 3.11+
- Django 5.2.7
- Django REST Framework

## 🛠️ Instalación Local

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

## 🌐 Endpoints

- `GET /api/stations/` - Lista todas las estaciones
- `GET /api/stations/{id}/` - Detalle de una estación
- `GET /api/stations/by_line/?line=Línea 1` - Estaciones por línea
- `GET /admin/` - Panel de administración

## 📝 Variables de Entorno

Crea un archivo `.env` con:

```
SECRET_KEY=tu-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True
```

## 🚀 Despliegue en Render

Este proyecto está configurado para desplegarse en Render. Ver la documentación de Render para más detalles.

