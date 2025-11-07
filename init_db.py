#!/usr/bin/env python
"""
Script único que inicializa todo: superusuario y estaciones
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command
from stations.models import Station

User = get_user_model()

def init_all():
    """Inicializa superusuario y estaciones"""
    
    print('=' * 60)
    print('🚀 INICIALIZANDO BASE DE DATOS')
    print('=' * 60)
    
    # 1. Crear/actualizar superusuario
    print('\n👤 Paso 1: Creando/actualizando superusuario...')
    try:
        username = 'admin'
        email = 'admin@metrolima.com'
        password = 'admin123'
        
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )
        
        if not created:
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
        
        user.set_password(password)
        user.save()
        
        print(f'✅ Superusuario: {username} / {password}')
    except Exception as e:
        print(f'⚠️ Error con superusuario: {e}')
    
    # 2. Migrar estaciones de "Línea 3" a "Metropolitano"
    print('\n📋 Paso 2: Migrando estaciones de "Línea 3" a "Metropolitano"...')
    try:
        stations_l3 = Station.objects.filter(line='Línea 3')
        count_l3 = stations_l3.count()
        
        if count_l3 > 0:
            updated = stations_l3.update(line='Metropolitano')
            print(f'✅ Se actualizaron {updated} estaciones de "Línea 3" a "Metropolitano"')
        else:
            print('  No se encontraron estaciones con "Línea 3"')
    except Exception as e:
        print(f'⚠️ Error al migrar estaciones: {e}')
    
    # 3. Poblar todas las estaciones (incluyendo corredores)
    print('\n📋 Paso 3: Poblando todas las estaciones (incluyendo corredores)...')
    try:
        call_command('populate_stations', verbosity=1)
        print('✅ Comando populate_stations ejecutado exitosamente')
    except Exception as e:
        print(f'❌ Error al poblar estaciones: {e}')
        import traceback
        traceback.print_exc()
        return False
    
    # 4. Verificar resultados
    print('\n📊 Paso 4: Verificando resultados...')
    try:
        total = Station.objects.count()
        print(f'\n📊 Total de estaciones en BD: {total}')
        
        # Contar por línea
        por_linea = {}
        for line in ['Línea 1', 'Línea 2', 'Metropolitano', 'Corredor Morado', 'Corredor Azul']:
            count = Station.objects.filter(line=line).count()
            por_linea[line] = count
            print(f'   - {line}: {count} estaciones')
        
        # Verificar que no queden estaciones con "Línea 3"
        remaining_l3 = Station.objects.filter(line='Línea 3').count()
        if remaining_l3 > 0:
            print(f'\n⚠️ ADVERTENCIA: Aún quedan {remaining_l3} estaciones con "Línea 3"')
        
        if total == 0:
            print('⚠️ ADVERTENCIA: No hay estaciones en la base de datos!')
            return False
        
        return True
    except Exception as e:
        print(f'❌ Error al verificar resultados: {e}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    try:
        success = init_all()
        print('\n' + '=' * 60)
        if success:
            print('✅ INICIALIZACIÓN COMPLETADA EXITOSAMENTE')
        else:
            print('⚠️ INICIALIZACIÓN COMPLETADA CON ERRORES')
        print('=' * 60)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f'\n❌ ERROR CRÍTICO: {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)

