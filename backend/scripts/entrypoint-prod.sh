#!/bin/bash
python3 backend/manage.py makemigrations --no-input
python3 backend/manage.py migrate --no-input

gunicorn --chdir backend core.wsgi
