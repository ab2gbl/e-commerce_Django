FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy and set the entrypoint
CMD sh -c "python manage.py makemigrations --noinput && \
           python manage.py migrate --noinput && \
           python manage.py collectstatic --noinput && \
           python manage.py loaddata data.json && \
           gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000"