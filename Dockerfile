# 1. Imagen base oficial de Python ligera
FROM python:3.11-slim

# 2. Evita archivos .pyc y fuerza logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Instala dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# 5. Copia e instala dependencias Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia el resto del codigo fuente
COPY . /app/

# 7. Expone el puerto 8000
EXPOSE 8000

# 8. Comando por defecto: migra y levanta con Gunicorn (servidor WSGI de produccion)
CMD ["sh", "-c", "python manage.py migrate && gunicorn Tienda.wsgi:application --bind 0.0.0.0:8000 --workers 2"]
