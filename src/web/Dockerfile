FROM python:3.11-slim

LABEL org.opencontainers.image.source=https://github.com/v-lastrucci-c/MII_CC_UGR
LABEL org.opencontainers.image.description="Container for AIChronos WEB"
LABEL org.opencontainers.image.licenses=MIT

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev gcc build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar Poetry utilizando pip
RUN pip install --no-cache-dir poetry

# Copiar los archivos de configuración de Poetry
COPY pyproject.toml ./

# Instalar las dependencias de la API
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copiar los archivos necesarios de la aplicación al contenedor
COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/
COPY tests/ ./tests/

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["sh", "-c", "flask init-db && flask run --host=0.0.0.0 --port=5000"]
