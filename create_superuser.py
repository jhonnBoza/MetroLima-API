#!/usr/bin/env python
"""
Script para crear o actualizar superusuario automáticamente
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

# Crear o actualizar superusuario
username = 'admin'
email = 'admin@metrolima.com'
password = 'admin123'

print('🔧 Iniciando creación/actualización de superusuario...')

try:
    with transaction.atomic():
        # Intentar obtener el usuario existente
        try:
            user = User.objects.get(username=username)
            created = False
            print(f'📋 Usuario "{username}" encontrado, actualizando...')
        except User.DoesNotExist:
            # Si no existe, crear uno nuevo
            user = User(username=username)
            created = True
            print(f'➕ Creando nuevo usuario "{username}"...')

        # Establecer todos los campos necesarios
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        if created:
            print(f'✅ Superusuario "{username}" creado exitosamente')
        else:
            print(f'✅ Superusuario "{username}" actualizado exitosamente')

        # Verificar que el usuario puede autenticarse
        user.refresh_from_db()
        if user.check_password(password):
            print(f'✅ Verificación: La contraseña es correcta')
        else:
            print(f'❌ ERROR: La contraseña no coincide después de guardar')
            sys.exit(1)

        # Mostrar información final
        print('')
        print('=' * 50)
        print('✅ CREDENCIALES DEL SUPERUSUARIO:')
        print(f'   Usuario: {username}')
        print(f'   Contraseña: {password}')
        print(f'   Email: {email}')
        print('=' * 50)

except Exception as e:
    print(f'❌ Error al crear/actualizar superusuario: {e}')
    import traceback
    traceback.print_exc()
    sys.exit(1)

