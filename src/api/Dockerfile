FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev gcc build-essential postgresql && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar Poetry utilizando pip
RUN pip install --no-cache-dir poetry

# Copiar los archivos de configuración de Poetry
COPY pyproject.toml ./

# Instalar las dependencias de la API
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copiar los archivos de la API al contenedor
COPY app/ ./app/
COPY tests/ ./tests/

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para ejecutar la API FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
