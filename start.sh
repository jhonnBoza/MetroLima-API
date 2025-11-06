#!/usr/bin/env bash
# Script de inicio que ejecuta migraciones antes de iniciar gunicorn

set -e

echo "=========================================="
echo "🚀 Iniciando aplicación Django"
echo "=========================================="

echo "📦 Paso 1: Verificando base de datos..."
python manage.py showmigrations 2>&1 | head -20 || echo "⚠️ No se pueden mostrar migraciones aún"

echo "📦 Paso 2: Ejecutando migraciones..."
python manage.py migrate --noinput

echo "📦 Paso 3: Verificando que las tablas existan..."
python -c "
import django
django.setup()
from django.db import connection
cursor = connection.cursor()
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table';\")
tables = [row[0] for row in cursor.fetchall()]
print(f'✅ Tablas encontradas: {len(tables)}')
if 'auth_user' in tables:
    print('✅ Tabla auth_user existe')
else:
    print('❌ ERROR: Tabla auth_user NO existe')
    exit(1)
" || {
    echo "❌ ERROR: Las tablas no se crearon correctamente"
    echo "🔄 Intentando crear tablas manualmente..."
    python manage.py migrate --run-syncdb --noinput
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

