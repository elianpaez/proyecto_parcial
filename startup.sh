#!/usr/bin/env bash

python manage.py migrate

gunicorn proyecto_parcial.wsgi:application