from django.db import models

class Station(models.Model):
    STATUS_CHOICES = [
        ('OPERATIONAL', 'Operativa'),
        ('MAINTENANCE', 'Mantenimiento'),
        ('CONSTRUCTION', 'Construcción'),
        ('CLOSED', 'Cerrada'),
    ]
    
    LINE_CHOICES = [
        ('Línea 1', 'Línea 1'),
        ('Línea 2', 'Línea 2'),
        ('Línea 3', 'Línea 3'),
    ]
    
    id = models.CharField(primary_key=True, max_length=50)  # "LIM-01"
    name = models.CharField(max_length=200)
    line = models.CharField(max_length=50, choices=LINE_CHOICES)  # "Línea 1", "Línea 2", etc.
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(blank=True)  # Descripción detallada
    opening_time = models.CharField(max_length=5, default="05:00")
    closing_time = models.CharField(max_length=5, default="23:00")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES,
        default='OPERATIONAL'
    )
    image_url = models.URLField(blank=True, null=True)  # URL de imagen externa
    image = models.ImageField(upload_to='stations/', blank=True, null=True)  # Imagen local
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['line', 'name']
        verbose_name = 'Estación'
        verbose_name_plural = 'Estaciones'
    
    def __str__(self):
        return f"{self.name} ({self.line})"
