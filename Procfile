web: python manage.py migrate --run-syncdb --noinput && python manage.py migrate --noinput && python init_db.py && gunicorn metrolima_api.wsgi:application --bind 0.0.0.0:$PORT
