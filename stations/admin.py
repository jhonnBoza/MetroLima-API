from django.contrib import admin
from .models import Station

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'line', 'status', 'updated_at']
    list_filter = ['line', 'status']
    search_fields = ['name', 'address', 'description', 'id']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Información Básica', {
            'fields': ('id', 'name', 'line', 'address')
        }),
        ('Ubicación', {
            'fields': ('latitude', 'longitude')
        }),
        ('Detalles', {
            'fields': ('description', 'opening_time', 'closing_time', 'status')
        }),
        ('Imágenes', {
            'fields': ('image', 'image_url')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )
