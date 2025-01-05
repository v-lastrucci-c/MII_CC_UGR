#!/bin/bash

# Salir si hay errores
set -e

echo "Construyendo y levantando el clúster..."
docker compose up --build -d

# Esperar unos segundos para la inicialización
echo "Esperando que los servicios estén listos..."
sleep 10

echo "Ejecutando tests de la aplicación web..."
docker exec aichronos-web poetry run task test

echo "Ejecutando tests de la API..."
docker exec aichronos-api poetry run task test

echo "Todos los tests se ejecutaron correctamente."

echo "Deteniendo el clúster..."
docker compose down
