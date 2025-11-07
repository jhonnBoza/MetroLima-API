#!/usr/bin/env bash
# Script de inicio para Render

set -e

echo "=========================================="
echo "🚀 Iniciando aplicación Django"
echo "=========================================="

# Ejecutar migraciones
echo "📦 Ejecutando migraciones..."
python manage.py migrate --run-syncdb --noinput
python manage.py migrate --noinput

# Iniciar servidor
echo "🚀 Iniciando servidor Gunicorn..."
exec gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120
