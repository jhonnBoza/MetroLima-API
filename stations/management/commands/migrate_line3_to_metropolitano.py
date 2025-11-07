"""
Comando de gestión para migrar estaciones de "Línea 3" a "Metropolitano"
Ejecutar: python manage.py migrate_line3_to_metropolitano
"""
from django.core.management.base import BaseCommand
from stations.models import Station


class Command(BaseCommand):
    help = 'Migra todas las estaciones de "Línea 3" a "Metropolitano"'

    def handle(self, *args, **options):
        # Obtener todas las estaciones con "Línea 3"
        stations = Station.objects.filter(line='Línea 3')
        
        count = stations.count()
        
        if count == 0:
            self.stdout.write(
                self.style.WARNING('No se encontraron estaciones con "Línea 3"')
            )
            return
        
        # Actualizar todas las estaciones
        updated = stations.update(line='Metropolitano')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Se actualizaron {updated} estaciones de "Línea 3" a "Metropolitano"'
            )
        )
        
        # Verificar que no queden estaciones con "Línea 3"
        remaining = Station.objects.filter(line='Línea 3').count()
        if remaining > 0:
            self.stdout.write(
                self.style.ERROR(
                    f'⚠ Advertencia: Aún quedan {remaining} estaciones con "Línea 3"'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('✓ Migración completada exitosamente')
            )

