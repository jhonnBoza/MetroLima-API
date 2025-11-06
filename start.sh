#!/usr/bin/env bash
# Script de inicio que ejecuta migraciones antes de iniciar gunicorn

set -e

echo "📦 Ejecutando migraciones..."
python manage.py migrate --noinput

echo "🚀 Iniciando servidor..."
exec gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120

