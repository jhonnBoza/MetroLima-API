"""
URL configuration for metrolima_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def root_view(request):
    """Vista simple para la raíz del sitio"""
    return JsonResponse({
        'message': 'MetroLima API',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/stations/',
        }
    })

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/', include('stations.urls')),
]

# Para servir archivos de media en desarrollo y producción
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
