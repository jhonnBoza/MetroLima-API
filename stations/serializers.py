from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Station
        fields = [
            'id', 'name', 'line', 'address', 'latitude', 'longitude',
            'description', 'opening_time', 'closing_time', 'status',
            'image_url', 'updated_at'
        ]
        read_only_fields = ['updated_at', 'created_at']
    
    def get_image_url(self, obj):
        # Si tiene imagen local, devolver URL completa
        if obj.image:
            request = self.context.get('request')
            if request:
                # Construir URL usando la IP local para que funcione desde Android
                image_url = request.build_absolute_uri(obj.image.url)
                # Reemplazar localhost con la IP local si está presente
                if 'localhost' in image_url or '127.0.0.1' in image_url:
                    # Obtener la IP del host desde la request
                    host = request.get_host()
                    # Si es localhost, usar la IP local configurada
                    if 'localhost' in host or '127.0.0.1' in host:
                        # Intentar obtener la IP real del servidor
                        # Por defecto usar 172.20.10.4 (IP del usuario)
                        base_url = f"http://172.20.10.4:8000"
                        image_url = base_url + obj.image.url
                return image_url
        # Si no, usar image_url directo
        return obj.image_url or ''
    
    def to_representation(self, instance):
        # Convertir Decimal a String para la API
        representation = super().to_representation(instance)
        representation['latitude'] = str(instance.latitude)
        representation['longitude'] = str(instance.longitude)
        return representation

