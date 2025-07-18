#!/bin/sh

# Optional: Wait for the database to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "PostgreSQL is up - continuing..."

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata data.json

# Start Gunicorn
exec gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000
