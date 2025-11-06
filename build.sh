#!/usr/bin/env bash
# Script de build para Render

set -o errexit  # Salir si hay un error

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate --noinput

# Recopilar archivos estáticos
python manage.py collectstatic --noinput --clear

