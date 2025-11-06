#!/usr/bin/env bash
# Script de inicio que ejecuta migraciones antes de iniciar gunicorn

# NO usar set -e aquí porque queremos manejar errores manualmente
set +e

echo "=========================================="
echo "🚀 Iniciando aplicación Django"
echo "=========================================="

echo "📦 Paso 1: Verificando base de datos..."
python manage.py showmigrations 2>&1 | head -20 || echo "⚠️ No se pueden mostrar migraciones aún"

echo "📦 Paso 2: Ejecutando migraciones FORZADAS..."
echo "   - Verificando ruta de base de datos..."
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
import django
django.setup()
from django.conf import settings
print(f'Ruta de BD: {settings.DATABASES[\"default\"][\"NAME\"]}')
print(f'Directorio existe: {os.path.exists(os.path.dirname(settings.DATABASES[\"default\"][\"NAME\"]))}')
"

echo "   - Aplicando todas las migraciones con syncdb (FORZADO)..."
# Forzar creación de todas las tablas
python manage.py migrate --run-syncdb --noinput 2>&1
MIGRATE_EXIT=$?

echo "   - Verificando resultado de migración (exit code: $MIGRATE_EXIT)..."

if [ $MIGRATE_EXIT -ne 0 ]; then
    echo "⚠️ Primera migración falló, intentando métodos alternativos..."
    # Método 1: Migración normal
    python manage.py migrate --noinput 2>&1
    # Método 2: Syncdb de nuevo
    python manage.py migrate --run-syncdb --noinput 2>&1
    # Método 3: Migración específica de stations
    python manage.py migrate stations --noinput 2>&1 || true
    # Método 4: Migración general de nuevo
    python manage.py migrate --noinput 2>&1
else
    echo "   - Migración inicial exitosa, aplicando migraciones adicionales..."
    python manage.py migrate stations --noinput 2>&1 || true
    python manage.py migrate --noinput 2>&1
fi

echo "📦 Paso 3: Verificando que las tablas existan..."
python -c "
import django
django.setup()
from django.db import connection
cursor = connection.cursor()
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table';\")
tables = [row[0] for row in cursor.fetchall()]
print(f'✅ Tablas encontradas: {len(tables)}')
print(f'   Tablas: {tables}')
required_tables = ['auth_user', 'stations_station', 'django_migrations', 'django_content_type', 'django_session']
missing = [t for t in required_tables if t not in tables]
if missing:
    print(f'❌ ERROR: Faltan tablas: {missing}')
    exit(1)
else:
    print('✅ Todas las tablas requeridas existen')
" || {
    echo "❌ ERROR: Las tablas no se crearon correctamente"
    echo "🔄 FORZANDO creación de todas las tablas (último intento)..."
    # Eliminar BD y empezar de cero
    rm -f db.sqlite3 db.sqlite3-journal 2>/dev/null || true
    # Crear todas las tablas desde cero
    python manage.py migrate --run-syncdb --noinput
    python manage.py migrate --noinput
    python manage.py migrate stations --noinput
    # Verificar nuevamente
    python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
import django
django.setup()
from django.db import connection
cursor = connection.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\";')
tables = [row[0] for row in cursor.fetchall()]
print(f'Tablas después del intento final: {tables}')
if 'auth_user' not in tables or 'stations_station' not in tables:
    print('❌ ERROR CRÍTICO: Las tablas aún no existen')
    exit(1)
    "
    if [ $? -ne 0 ]; then
        echo "❌❌❌ ERROR CRÍTICO: No se pudieron crear las tablas"
        echo "🔄 Mostrando estado de migraciones..."
        python manage.py showmigrations
        exit(1)
    fi
}

echo "✅ Migraciones completadas correctamente"

echo "👤 Paso 4: Verificando superusuario..."
python -c "
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    print('⚠️ No existe superusuario, creando uno...')
    User.objects.create_superuser('admin', 'admin@metrolima.com', 'admin123')
    print('✅ Superusuario creado: admin / admin123')
else:
    print('✅ Superusuario ya existe')
" || echo "⚠️ No se pudo verificar/crear superusuario (puede ser normal si ya existe)"

echo "🚀 Paso 5: Iniciando servidor Gunicorn..."
exec gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120

