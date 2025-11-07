web: python manage.py migrate --run-syncdb --noinput && python manage.py migrate --noinput && (python create_superuser.py || true) && (python populate_stations.py || true) && gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT



