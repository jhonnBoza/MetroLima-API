#!/usr/bin/env bash
# Script para ejecutar migraciones manualmente en Render
# Úsalo si las migraciones no se ejecutan automáticamente

python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

