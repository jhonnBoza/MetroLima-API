#!/usr/bin/env bash
# Script de inicio para Render
# Este script fuerza el uso del comando correcto

exec gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120

