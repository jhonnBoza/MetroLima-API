from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Station
from .serializers import StationSerializer

class StationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para estaciones.
    ReadOnly porque Android solo necesita leer datos (por ahora).
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    
    def get_serializer_context(self):
        # Pasar request al serializer para generar URLs completas
        return {'request': self.request}
    
    @action(detail=False, methods=['get'], url_path='by_line')
    def by_line(self, request):
        """
        GET /api/stations/by_line/?line=Línea 1
        Obtiene estaciones filtradas por línea
        """
        line = request.query_params.get('line', None)
        if line:
            stations = Station.objects.filter(line=line)
            serializer = self.get_serializer(stations, many=True)
            return Response(serializer.data)
        return Response([])
