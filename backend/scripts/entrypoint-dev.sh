#!/bin/bash
python manage.py wait_for_db

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:$PORT
