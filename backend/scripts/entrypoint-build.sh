#!/bin/bash
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

cd backend

python manage.py collectstatic --no-input

python manage.py makemigrations --no-input

python manage.py migrate --no-input

gunicorn core.wsgi:application -b 0.0.0.0:$PORT
