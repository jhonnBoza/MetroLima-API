#!/usr/bin/env python
"""
Script para crear superusuario automáticamente si no existe
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Crear superusuario si no existe
username = 'admin'
email = 'admin@metrolima.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    try:
        User.objects.create_superuser(username, email, password)
        print(f'✅ Superusuario creado: {username} / {password}')
    except Exception as e:
        print(f'⚠️ Error al crear superusuario: {e}')
        sys.exit(1)
else:
    print(f'✅ Superusuario "{username}" ya existe')

