from django.core.management.base import BaseCommand
from stations.models import Station

class Command(BaseCommand):
    help = 'Agrega todas las estaciones del Metro de Lima a la base de datos'

    def handle(self, *args, **options):
        # Estaciones de la Línea 1 - Villa El Salvador a San Juan de Lurigancho
        linea1_stations = [
            {
                'id': 'LIM-01',
                'name': 'Villa El Salvador',
                'line': 'Línea 1',
                'address': 'Av. Villa El Salvador',
                'latitude': -12.1939,
                'longitude': -76.9399,
                'description': 'Terminal sur de la Línea 1',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-02',
                'name': 'María Auxiliadora',
                'line': 'Línea 1',
                'address': 'Av. María Auxiliadora',
                'latitude': -12.1639,
                'longitude': -76.9703,
                'description': 'Conexión con buses',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-03',
                'name': 'La Cultura',
                'line': 'Línea 1',
                'address': 'Av. La Cultura',
                'latitude': -12.0865,
                'longitude': -76.9779,
                'description': 'Cerca al parque',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-04',
                'name': 'San Borja Sur',
                'line': 'Línea 1',
                'address': 'Av. San Borja Sur',
                'latitude': -12.1003,
                'longitude': -76.9961,
                'description': 'Distrito San Borja',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-05',
                'name': 'Angamos',
                'line': 'Línea 1',
                'address': 'Av. Angamos',
                'latitude': -12.1214,
                'longitude': -77.0297,
                'description': 'Conexión con Línea 2',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-06',
                'name': 'San Borja Norte',
                'line': 'Línea 1',
                'address': 'Av. San Borja Norte',
                'latitude': -12.0800,
                'longitude': -76.9800,
                'description': 'Centro de San Borja',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-07',
                'name': 'La Victoria',
                'line': 'Línea 1',
                'address': 'Av. La Victoria',
                'latitude': -12.0600,
                'longitude': -77.0200,
                'description': 'Distrito comercial',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-08',
                'name': 'Gamarra',
                'line': 'Línea 1',
                'address': 'Av. Gamarra',
                'latitude': -12.0450,
                'longitude': -77.0200,
                'description': 'Centro comercial',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-09',
                'name': 'El Agustino',
                'line': 'Línea 1',
                'address': 'Av. El Agustino',
                'latitude': -12.0200,
                'longitude': -77.0000,
                'description': 'Zona residencial',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-10',
                'name': 'San Juan de Lurigancho',
                'line': 'Línea 1',
                'address': 'Av. San Juan de Lurigancho',
                'latitude': -11.9800,
                'longitude': -77.0700,
                'description': 'Terminal norte',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
        ]

        # Estaciones de la Línea 2 - Ate Vitarte a Callao
        linea2_stations = [
            {
                'id': 'LIM-11',
                'name': 'Ate Vitarte',
                'line': 'Línea 2',
                'address': 'Av. Ate Vitarte',
                'latitude': -12.0450,
                'longitude': -76.9500,
                'description': 'Terminal este',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-12',
                'name': 'Santa Anita',
                'line': 'Línea 2',
                'address': 'Av. Santa Anita',
                'latitude': -12.0500,
                'longitude': -76.9600,
                'description': 'Distrito Santa Anita',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-13',
                'name': 'La Molina',
                'line': 'Línea 2',
                'address': 'Av. La Molina',
                'latitude': -12.0500,
                'longitude': -76.9500,
                'description': 'Zona residencial',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-14',
                'name': 'San Luis',
                'line': 'Línea 2',
                'address': 'Av. San Luis',
                'latitude': -12.0600,
                'longitude': -76.9700,
                'description': 'Distrito San Luis',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-15',
                'name': 'San Isidro',
                'line': 'Línea 2',
                'address': 'Av. San Isidro',
                'latitude': -12.0850,
                'longitude': -77.0370,
                'description': 'Distrito financiero',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-16',
                'name': 'Miraflores',
                'line': 'Línea 2',
                'address': 'Av. Miraflores',
                'latitude': -12.1214,
                'longitude': -77.0297,
                'description': 'Zona turística',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-17',
                'name': 'Barranco',
                'line': 'Línea 2',
                'address': 'Av. Barranco',
                'latitude': -12.1440,
                'longitude': -77.0200,
                'description': 'Barranco cultural',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-18',
                'name': 'Chorrillos',
                'line': 'Línea 2',
                'address': 'Av. Chorrillos',
                'latitude': -12.1600,
                'longitude': -77.0100,
                'description': 'Distrito Chorrillos',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-19',
                'name': 'San Miguel',
                'line': 'Línea 2',
                'address': 'Av. San Miguel',
                'latitude': -12.0600,
                'longitude': -77.1100,
                'description': 'Acceso al puerto',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'LIM-20',
                'name': 'Callao',
                'line': 'Línea 2',
                'address': 'Av. Callao',
                'latitude': -12.0500,
                'longitude': -77.1300,
                'description': 'Terminal oeste',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
        ]

        # Estaciones del Metropolitano - En construcción
        linea3_stations = [
            {
                'id': 'LIM-21',
                'name': 'Comas',
                'line': 'Metropolitano',
                'address': 'Av. Comas',
                'latitude': -11.9800,
                'longitude': -77.0700,
                'description': 'Norte de Lima',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-22',
                'name': 'Independencia',
                'line': 'Metropolitano',
                'address': 'Av. Independencia',
                'latitude': -12.0000,
                'longitude': -77.0500,
                'description': 'Distrito Independencia',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-23',
                'name': 'Rímac',
                'line': 'Metropolitano',
                'address': 'Av. Rímac',
                'latitude': -12.0200,
                'longitude': -77.0300,
                'description': 'Distrito Rímac',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-24',
                'name': 'Cercado de Lima',
                'line': 'Metropolitano',
                'address': 'Av. Cercado',
                'latitude': -12.0464,
                'longitude': -77.0428,
                'description': 'Centro histórico',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-25',
                'name': 'La Victoria',
                'line': 'Metropolitano',
                'address': 'Av. La Victoria',
                'latitude': -12.0600,
                'longitude': -77.0200,
                'description': 'Distrito comercial',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-26',
                'name': 'Lince',
                'line': 'Metropolitano',
                'address': 'Av. Lince',
                'latitude': -12.0800,
                'longitude': -77.0300,
                'description': 'Distrito Lince',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-27',
                'name': 'Jesús María',
                'line': 'Metropolitano',
                'address': 'Av. Jesús María',
                'latitude': -12.0900,
                'longitude': -77.0400,
                'description': 'Distrito Jesús María',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-28',
                'name': 'Magdalena',
                'line': 'Metropolitano',
                'address': 'Av. Magdalena',
                'latitude': -12.1000,
                'longitude': -77.0500,
                'description': 'Distrito Magdalena',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-29',
                'name': 'Pueblo Libre',
                'line': 'Metropolitano',
                'address': 'Av. Pueblo Libre',
                'latitude': -12.0950,
                'longitude': -77.0600,
                'description': 'Barrio tradicional',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
            {
                'id': 'LIM-30',
                'name': 'Chorrillos',
                'line': 'Metropolitano',
                'address': 'Av. Chorrillos',
                'latitude': -12.1600,
                'longitude': -77.0100,
                'description': 'Terminal sur',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'CONSTRUCTION'
            },
        ]

        # Combinar todas las estaciones
        all_stations = linea1_stations + linea2_stations + linea3_stations

        # Agregar estaciones a la base de datos
        created_count = 0
        updated_count = 0

        for station_data in all_stations:
            station, created = Station.objects.update_or_create(
                id=station_data['id'],
                defaults={
                    'name': station_data['name'],
                    'line': station_data['line'],
                    'address': station_data['address'],
                    'latitude': station_data['latitude'],
                    'longitude': station_data['longitude'],
                    'description': station_data['description'],
                    'opening_time': station_data['opening_time'],
                    'closing_time': station_data['closing_time'],
                    'status': station_data['status'],
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'[OK] Creada: {station.name} ({station.line})')
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'[ACT] Actualizada: {station.name} ({station.line})')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n[COMPLETADO] Proceso finalizado!\n'
                f'   - Estaciones creadas: {created_count}\n'
                f'   - Estaciones actualizadas: {updated_count}\n'
                f'   - Total: {len(all_stations)} estaciones'
            )
        )

