web: python manage.py migrate --run-syncdb --noinput; python manage.py migrate --noinput; (python create_superuser.py || true); (python manage.py populate_stations || true); gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT



