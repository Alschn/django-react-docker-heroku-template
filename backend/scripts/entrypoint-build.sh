#!/bin/bash
cd backend

python manage.py wait_for_db

python manage.py collectstatic --no-input

python manage.py makemigrations --no-input

python manage.py migrate --no-input

gunicorn core.wsgi:application -b 0.0.0.0:$PORT
