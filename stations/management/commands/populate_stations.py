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

        # Estaciones del Corredor Morado - Rutas 404, 405, 409
        corredor_morado_stations = [
            {
                'id': 'CM-01',
                'name': 'La Capilla',
                'line': 'Corredor Morado',
                'address': 'Terminal Norte (SJL)',
                'latitude': -11.9685000,
                'longitude': -77.0001000,
                'description': 'Terminal Norte - San Juan de Lurigancho',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-02',
                'name': 'Montenegro',
                'line': 'Corredor Morado',
                'address': 'SJL',
                'latitude': -11.9655000,
                'longitude': -77.0005000,
                'description': 'Paradero Montenegro',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-03',
                'name': 'La Cuatro',
                'line': 'Corredor Morado',
                'address': 'SJL',
                'latitude': -11.9575000,
                'longitude': -76.9950000,
                'description': 'Paradero La Cuatro',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-04',
                'name': 'Bayóvar',
                'line': 'Corredor Morado',
                'address': 'SJL - Integración Línea 1',
                'latitude': -11.9560733,
                'longitude': -76.9940003,
                'description': 'Integración con Línea 1 Metro',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-05',
                'name': 'Celima',
                'line': 'Corredor Morado',
                'address': 'SJL',
                'latitude': -11.9330000,
                'longitude': -77.0080000,
                'description': 'Paradero Celima',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-06',
                'name': 'Mercado de Flores',
                'line': 'Corredor Morado',
                'address': 'Av. Abancay',
                'latitude': -12.0520000,
                'longitude': -77.0295000,
                'description': 'Paradero troncal compartido - Rutas 404, 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-07',
                'name': 'Acho',
                'line': 'Corredor Morado',
                'address': 'Av. Abancay',
                'latitude': -12.0400000,
                'longitude': -77.0255000,
                'description': 'Paradero troncal compartido - Rutas 404, 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-08',
                'name': 'Cuzco',
                'line': 'Corredor Morado',
                'address': 'Av. Abancay',
                'latitude': -12.0515000,
                'longitude': -77.0298000,
                'description': 'Paradero troncal compartido - Rutas 404, 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-09',
                'name': 'Grau (Nuevo)',
                'line': 'Corredor Morado',
                'address': 'Eje Av. Abancay',
                'latitude': -12.0560000,
                'longitude': -77.0310000,
                'description': 'Eje Av. Abancay - Ubicación Reubicada',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-10',
                'name': 'Plaza Bolognesi',
                'line': 'Corredor Morado',
                'address': 'Eje Central - Cruce Av. Garcilaso',
                'latitude': -12.0620000,
                'longitude': -77.0375000,
                'description': 'Eje Central, Cruce Av. Garcilaso',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-11',
                'name': '28 de Julio',
                'line': 'Corredor Morado',
                'address': 'Av. 28 de Julio',
                'latitude': -12.0640000,
                'longitude': -77.0320000,
                'description': 'Paradero troncal - Rutas 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-12',
                'name': 'Unanue',
                'line': 'Corredor Morado',
                'address': 'Av. 28 de Julio',
                'latitude': -12.0665000,
                'longitude': -77.0318000,
                'description': 'Paradero troncal - Rutas 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-13',
                'name': 'Católica',
                'line': 'Corredor Morado',
                'address': 'Av. 28 de Julio',
                'latitude': -12.0710000,
                'longitude': -77.0315000,
                'description': 'Paradero troncal - Rutas 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-14',
                'name': 'México',
                'line': 'Corredor Morado',
                'address': 'Av. 28 de Julio',
                'latitude': -12.0785000,
                'longitude': -77.0310000,
                'description': 'Paradero troncal - Rutas 405, 409',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-15',
                'name': 'Hospital PNP',
                'line': 'Corredor Morado',
                'address': 'Av. 28 de Julio / Av. Arica',
                'latitude': -12.0805000,
                'longitude': -77.0460000,
                'description': 'Ruta 404 - Av. 28 de Julio / Av. Arica',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-16',
                'name': 'Pardo de Zela',
                'line': 'Corredor Morado',
                'address': 'Lince',
                'latitude': -12.0835000,
                'longitude': -77.0345000,
                'description': 'Paradero Pardo de Zela',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-17',
                'name': 'Javier Prado',
                'line': 'Corredor Morado',
                'address': 'San Isidro',
                'latitude': -12.0945000,
                'longitude': -77.0360000,
                'description': 'Paradero Javier Prado',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-18',
                'name': 'La Virgen',
                'line': 'Corredor Morado',
                'address': 'Terminal Oeste (Magdalena)',
                'latitude': -12.0950000,
                'longitude': -77.0760000,
                'description': 'Terminal Oeste - Magdalena',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CM-19',
                'name': 'Carnaval y Moreyra',
                'line': 'Corredor Morado',
                'address': 'Terminal Sur (San Isidro)',
                'latitude': -12.1005000,
                'longitude': -77.0395000,
                'description': 'Terminal Sur - San Isidro',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
        ]

        # Estaciones del Corredor Azul - Servicio Troncal 301 y Rutas Complementarias
        corredor_azul_stations = [
            {
                'id': 'CA-01',
                'name': 'Amancaes',
                'line': 'Corredor Azul',
                'address': 'Rímac',
                'latitude': -12.01630,
                'longitude': -77.02100,
                'description': 'Terminal Norte - Rímac',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-02',
                'name': 'La Colonia',
                'line': 'Corredor Azul',
                'address': 'Rímac',
                'latitude': -12.02550,
                'longitude': -77.02750,
                'description': 'Paradero La Colonia',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-03',
                'name': 'Chira',
                'line': 'Corredor Azul',
                'address': 'Rímac',
                'latitude': -12.03450,
                'longitude': -77.03350,
                'description': 'Paradero Chira',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-04',
                'name': 'Virú',
                'line': 'Corredor Azul',
                'address': 'Cercado de Lima',
                'latitude': -12.04000,
                'longitude': -77.03480,
                'description': 'Paradero Virú',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-05',
                'name': 'E. Villar',
                'line': 'Corredor Azul',
                'address': 'Lince',
                'latitude': -12.06200,
                'longitude': -77.03900,
                'description': 'Paradero E. Villar',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-06',
                'name': 'Manuel Segura',
                'line': 'Corredor Azul',
                'address': 'Lince',
                'latitude': -12.07250,
                'longitude': -77.03780,
                'description': 'Paradero Manuel Segura',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-07',
                'name': 'Tomás Guido',
                'line': 'Corredor Azul',
                'address': 'Lince',
                'latitude': -12.08310,
                'longitude': -77.03850,
                'description': 'Paradero Tomás Guido',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-08',
                'name': 'Angamos',
                'line': 'Corredor Azul',
                'address': 'Miraflores',
                'latitude': -12.10090,
                'longitude': -77.03510,
                'description': 'Paradero Angamos',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-09',
                'name': 'Piura',
                'line': 'Corredor Azul',
                'address': 'Miraflores',
                'latitude': -12.11050,
                'longitude': -77.03250,
                'description': 'Paradero Piura',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-10',
                'name': 'Pardo',
                'line': 'Corredor Azul',
                'address': 'Miraflores',
                'latitude': -12.11500,
                'longitude': -77.03050,
                'description': 'Paradero Pardo - Terminal 336',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-11',
                'name': 'Larco',
                'line': 'Corredor Azul',
                'address': 'Miraflores',
                'latitude': -12.12050,
                'longitude': -77.02700,
                'description': 'Paradero Larco',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-12',
                'name': 'Balta',
                'line': 'Corredor Azul',
                'address': 'Barranco',
                'latitude': -12.13700,
                'longitude': -77.02270,
                'description': 'Paradero Balta',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-13',
                'name': 'Plaza Butters',
                'line': 'Corredor Azul',
                'address': 'Terminal Sur (Barranco)',
                'latitude': -12.13810,
                'longitude': -77.02250,
                'description': 'Terminal Sur - Barranco',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-14',
                'name': 'El Sol',
                'line': 'Corredor Azul',
                'address': 'Barranco',
                'latitude': -12.13850,
                'longitude': -77.02245,
                'description': 'Paradero El Sol (Plaza Butters inicio)',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-15',
                'name': 'Schell',
                'line': 'Corredor Azul',
                'address': 'Miraflores',
                'latitude': -12.11210,
                'longitude': -77.03150,
                'description': 'Paradero Schell',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-16',
                'name': 'Juan De Arona',
                'line': 'Corredor Azul',
                'address': 'San Isidro',
                'latitude': -12.09100,
                'longitude': -77.03680,
                'description': 'Paradero Juan De Arona',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-17',
                'name': 'Manuel Segura (Vuelta)',
                'line': 'Corredor Azul',
                'address': 'Lince',
                'latitude': -12.07150,
                'longitude': -77.03800,
                'description': 'Paradero Manuel Segura - Vuelta',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-18',
                'name': 'Saco Oliveros',
                'line': 'Corredor Azul',
                'address': 'Cercado de Lima',
                'latitude': -12.05950,
                'longitude': -77.03880,
                'description': 'Paradero Saco Oliveros',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-19',
                'name': 'España',
                'line': 'Corredor Azul',
                'address': 'Cercado de Lima',
                'latitude': -12.04610,
                'longitude': -77.03600,
                'description': 'Paradero España',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-20',
                'name': 'Pizarro',
                'line': 'Corredor Azul',
                'address': 'Rímac',
                'latitude': -12.03700,
                'longitude': -77.03450,
                'description': 'Paradero Pizarro',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-21',
                'name': '24 De Junio',
                'line': 'Corredor Azul',
                'address': 'Terminal Norte (Rímac)',
                'latitude': -12.01590,
                'longitude': -77.02050,
                'description': 'Terminal Norte - Rímac',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-22',
                'name': 'D. Casanova',
                'line': 'Corredor Azul',
                'address': 'Cerca de la Av. Arequipa',
                'latitude': -12.08750,
                'longitude': -77.03750,
                'description': 'Ruta 303 - Cerca de la Av. Arequipa',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
            {
                'id': 'CA-23',
                'name': 'Uruguay',
                'line': 'Corredor Azul',
                'address': 'Cerca de la Av. Arequipa',
                'latitude': -12.05350,
                'longitude': -77.03890,
                'description': 'Ruta 303 - Cerca de la Av. Arequipa',
                'opening_time': '05:00',
                'closing_time': '23:00',
                'status': 'OPERATIONAL'
            },
        ]

        # Combinar todas las estaciones
        all_stations = linea1_stations + linea2_stations + linea3_stations + corredor_morado_stations + corredor_azul_stations

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

