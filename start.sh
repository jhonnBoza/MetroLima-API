#!/usr/bin/env bash
# Script de inicio que ejecuta migraciones antes de iniciar gunicorn

set -e

echo "📦 Verificando base de datos..."
# Asegurar que el directorio existe
mkdir -p /opt/render/project/src 2>/dev/null || true

echo "📦 Ejecutando migraciones..."
python manage.py migrate --noinput || {
    echo "⚠️ Error en migraciones, intentando de nuevo..."
    python manage.py migrate --noinput --run-syncdb
}

echo "✅ Migraciones completadas"
echo "🚀 Iniciando servidor..."
exec gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120

