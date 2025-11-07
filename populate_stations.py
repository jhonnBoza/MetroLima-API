#!/usr/bin/env python
"""
Script para cargar todas las estaciones del Metro de Lima desde JSON
"""
import os
import sys
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')
django.setup()

from stations.models import Station

def populate_stations():
    """Carga todas las estaciones desde el archivo JSON"""
    
    # Obtener la ruta del archivo JSON
    # Intentar varias rutas posibles
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
    
    print('🚀 Iniciando carga de estaciones desde JSON...')
    print(f'📁 Directorio actual: {os.getcwd()}')
    print(f'📁 Directorio del script: {base_dir}')
    
    if not json_path:
        print(f'❌ ERROR: No se encontró el archivo stations_data.json')
        print(f'   Buscado en: {possible_paths}')
        print(f'   Archivos en directorio actual: {os.listdir(os.getcwd())}')
        sys.exit(1)
    
    print(f'✅ Archivo encontrado: {json_path}')
    
    # Leer el archivo JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            all_stations = json.load(f)
    except FileNotFoundError:
        print(f'❌ ERROR: No se encontró el archivo {json_path}')
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f'❌ ERROR: El archivo JSON tiene un formato inválido: {e}')
        sys.exit(1)
    
    print(f'📋 Total de estaciones a cargar: {len(all_stations)}')
    print('')
    
    # Agregar estaciones a la base de datos
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
                print(f'✅ Creada: {station.name} ({station.line})')
            else:
                updated_count += 1
                print(f'🔄 Actualizada: {station.name} ({station.line})')
        except Exception as e:
            print(f'❌ Error al crear {station_data.get("name", "desconocida")}: {e}')
    
    print('')
    print('=' * 50)
    print('✅ CARGA DE ESTACIONES COMPLETADA')
    print(f'   - Estaciones creadas: {created_count}')
    print(f'   - Estaciones actualizadas: {updated_count}')
    print(f'   - Total procesadas: {len(all_stations)}')
    print('=' * 50)

if __name__ == '__main__':
    try:
        populate_stations()
    except Exception as e:
        print(f'❌ Error crítico: {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)
