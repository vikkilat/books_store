#!/bin/bash

echo "--START MAKEMIGRATIONS--"
python manage.py makemigrations
sleep 2
echo "--END MAKEMIGRATIONS--"

echo "--START MIGRATE--"
python manage.py migrate
sleep 2
echo "--END MIGRATE--"

echo "--START CREATE SUPER USER--"
export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
python manage.py createsuperuser --no-input
echo "--END CREATE SUPER USER--"

exec "$@"
