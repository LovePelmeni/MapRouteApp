#!/bin/sh

echo "Running Application..."
python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --no-input &&
gunicorn GeoProject.wsgi:application --bind 0.0.0.0 --workers 5 --timeout 120




