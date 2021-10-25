#!/bin/sh
python manage.py makemigrations
python manage.py makemigrations backend
python manage.py migrate
exec "$@"