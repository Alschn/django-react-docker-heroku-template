#!/bin/bash
python ./backend/manage.py makemigrations --no-input
python ./backend/manage.py migrate --no-input

