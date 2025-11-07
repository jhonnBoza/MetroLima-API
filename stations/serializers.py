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
                # Construir URL completa usando el dominio de la request
                # Esto funciona tanto en desarrollo local como en Render
                return request.build_absolute_uri(obj.image.url)
        # Si no, usar image_url directo (URL externa)
        return obj.image_url or ''
    
    def to_representation(self, instance):
        # Convertir Decimal a String para la API
        representation = super().to_representation(instance)
        representation['latitude'] = str(instance.latitude)
        representation['longitude'] = str(instance.longitude)
        return representation

