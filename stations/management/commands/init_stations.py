"""
Comando de gestión para inicializar todas las estaciones
Ejecuta: python manage.py init_stations

Este comando:
1. Migra estaciones de "Línea 3" a "Metropolitano"
2. Pobla todas las estaciones (incluyendo corredores)
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command
from stations.models import Station


class Command(BaseCommand):
    help = 'Inicializa todas las estaciones: migra Línea 3 a Metropolitano y pobla todas las estaciones'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('INICIALIZACIÓN DE ESTACIONES'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        
        # Paso 1: Migrar estaciones de "Línea 3" a "Metropolitano"
        self.stdout.write(self.style.WARNING('\n[PASO 1] Migrando estaciones de "Línea 3" a "Metropolitano"...'))
        stations_l3 = Station.objects.filter(line='Línea 3')
        count_l3 = stations_l3.count()
        
        if count_l3 > 0:
            updated = stations_l3.update(line='Metropolitano')
            self.stdout.write(
                self.style.SUCCESS(f'✓ Se actualizaron {updated} estaciones de "Línea 3" a "Metropolitano"')
            )
        else:
            self.stdout.write(
                self.style.WARNING('  No se encontraron estaciones con "Línea 3"')
            )
        
        # Paso 2: Poblar todas las estaciones
        self.stdout.write(self.style.WARNING('\n[PASO 2] Poblando todas las estaciones...'))
        try:
            call_command('populate_stations')
            self.stdout.write(self.style.SUCCESS('✓ Comando populate_stations ejecutado exitosamente'))
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'✗ Error al ejecutar populate_stations: {e}')
            )
            raise
        
        # Paso 3: Verificar resultados
        self.stdout.write(self.style.WARNING('\n[PASO 3] Verificando resultados...'))
        total = Station.objects.count()
        por_linea = {}
        for line in ['Línea 1', 'Línea 2', 'Metropolitano', 'Corredor Morado', 'Corredor Azul']:
            count = Station.objects.filter(line=line).count()
            por_linea[line] = count
            self.stdout.write(f'  {line}: {count} estaciones')
        
        # Verificar que no queden estaciones con "Línea 3"
        remaining_l3 = Station.objects.filter(line='Línea 3').count()
        if remaining_l3 > 0:
            self.stdout.write(
                self.style.ERROR(f'\n⚠ ADVERTENCIA: Aún quedan {remaining_l3} estaciones con "Línea 3"')
            )
        
        self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
        self.stdout.write(self.style.SUCCESS(f'✓ INICIALIZACIÓN COMPLETADA'))
        self.stdout.write(self.style.SUCCESS(f'  Total de estaciones: {total}'))
        self.stdout.write(self.style.SUCCESS('=' * 60))

