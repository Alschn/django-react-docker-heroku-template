#!/bin/bash
python3 backend/manage.py makemigrations --no-input
python3 backend/manage.py migrate --no-input

python3 backend/manage.py runserver 0.0.0.0:$PORT
