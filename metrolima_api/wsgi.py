"""
WSGI config for metrolima_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metrolima_api.settings')

# Ejecutar migraciones automáticamente al iniciar si las tablas no existen
try:
    application = get_wsgi_application()
    
    # Verificar si las tablas existen
    from django.db import connection
    from django.conf import settings
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    try:
        if 'sqlite' in db_engine:
            # Para SQLite
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user';")
            tables = cursor.fetchall()
        else:
            # Para PostgreSQL y otras BDs
            cursor = connection.cursor()
            cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename='auth_user';")
            tables = cursor.fetchall()
        
        if not tables:
            print("⚠️ Tabla auth_user no existe, ejecutando migraciones automáticamente...")
            from django.core.management import call_command
            call_command('migrate', '--run-syncdb', verbosity=1, interactive=False)
            print("✅ Migraciones ejecutadas desde wsgi.py")
        else:
            print("✅ Base de datos ya tiene las tablas necesarias")
    except Exception as e:
        print(f"⚠️ Error verificando tablas: {e}")
        # Intentar ejecutar migraciones de todas formas
        try:
            from django.core.management import call_command
            call_command('migrate', '--run-syncdb', verbosity=1, interactive=False)
            print("✅ Migraciones ejecutadas desde wsgi.py (fallback)")
        except Exception as migrate_error:
            print(f"❌ Error ejecutando migraciones: {migrate_error}")
except Exception as e:
    print(f"❌ Error inicializando aplicación: {e}")
    import traceback
    traceback.print_exc()
    # Aún así, crear la aplicación para que el servidor inicie
    application = get_wsgi_application()
