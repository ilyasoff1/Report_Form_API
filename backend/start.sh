#!/bin/bash

python manage.py migrate --noinput

#python manage.py collectstatic --noinput

python manage.py create_superuser

python manage.py runserver 0.0.0.0:8002

#gunicorn portal.wsgi:application --bind 0.0.0.0:8002