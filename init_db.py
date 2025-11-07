#!/usr/bin/env python
"""
Script único que inicializa todo: superusuario y estaciones
"""
import os
import sys
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
django.setup()

from django.contrib.auth import get_user_model
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
    
    # 2. Cargar estaciones desde JSON
    print('\n📋 Paso 2: Cargando estaciones desde JSON...')
    
    # Buscar el archivo JSON
    base_dir = os.path.dirname(os.path.abspath(__file__))
    possible_paths = [
        os.path.join(base_dir, 'stations_data.json'),
        os.path.join(os.getcwd(), 'stations_data.json'),
        'stations_data.json',
    ]
    
    json_path = None
    for path in possible_paths:
        if os.path.exists(path):
            json_path = path
            break
    
    if not json_path:
        print(f'❌ ERROR: No se encontró stations_data.json')
        print(f'   Buscado en: {possible_paths}')
        return False
    
    print(f'✅ Archivo encontrado: {json_path}')
    
    # Leer y cargar estaciones
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            all_stations = json.load(f)
        
        print(f'📊 Total de estaciones en JSON: {len(all_stations)}')
        
        created_count = 0
        updated_count = 0
        
        for station_data in all_stations:
            try:
                station, created = Station.objects.update_or_create(
                    id=station_data['id'],
                    defaults={
                        'name': station_data['name'],
                        'line': station_data['line'],
                        'address': station_data['address'],
                        'latitude': station_data['latitude'],
                        'longitude': station_data['longitude'],
                        'description': station_data.get('description', ''),
                        'opening_time': station_data.get('opening_time', '05:00'),
                        'closing_time': station_data.get('closing_time', '23:00'),
                        'status': station_data.get('status', 'OPERATIONAL'),
                    }
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1
            except Exception as e:
                print(f'❌ Error con {station_data.get("name", "desconocida")}: {e}')
        
        print(f'\n✅ Estaciones cargadas:')
        print(f'   - Creadas: {created_count}')
        print(f'   - Actualizadas: {updated_count}')
        print(f'   - Total: {len(all_stations)}')
        
        # Verificar que se guardaron
        total_in_db = Station.objects.count()
        print(f'\n📊 Total de estaciones en BD: {total_in_db}')
        
        if total_in_db == 0:
            print('⚠️ ADVERTENCIA: No hay estaciones en la base de datos!')
            return False
        
        return True
        
    except Exception as e:
        print(f'❌ Error al cargar estaciones: {e}')
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

