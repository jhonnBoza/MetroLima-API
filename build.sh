#!/usr/bin/env bash
# Script de build para Render
# Este script se ejecuta durante el build en Render

set -o errexit  # Salir si hay un error
set -o pipefail # Capturar errores en pipes

echo "🔧 Instalando dependencias..."
pip install -r requirements.txt

echo "📦 Ejecutando migraciones..."
# Asegurar que el directorio de la base de datos exista
mkdir -p $(dirname db.sqlite3) 2>/dev/null || true

# Ejecutar migraciones (esto crea todas las tablas necesarias)
python manage.py migrate --noinput

echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "✅ Build completado"

