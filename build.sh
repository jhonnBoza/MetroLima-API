#!/usr/bin/env bash
# Script de build para Render
# Este script se ejecuta durante el build en Render

set -o errexit  # Salir si hay un error
set -o pipefail # Capturar errores en pipes

echo "🔧 Instalando dependencias..."
pip install -r requirements.txt

echo "📦 Ejecutando migraciones..."
python manage.py migrate --noinput || echo "⚠️ Advertencia: Error en migraciones (puede ser normal si la BD no existe aún)"

echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput --clear || echo "⚠️ Advertencia: Error al recopilar estáticos"

echo "✅ Build completado"

