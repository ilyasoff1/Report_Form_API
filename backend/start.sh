#!/bin/bash

python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8082

#gunicorn portal.wsgi:application --bind 0.0.0.0:8002