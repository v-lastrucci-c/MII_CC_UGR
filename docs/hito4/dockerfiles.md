# Documentación de los Dockerfiles

## **1. Dockerfile para la Aplicación AIChronos**
### **Propósito**:
El Dockerfile para la aplicación AIChronos define el entorno necesario para ejecutar la aplicación web desarrollada en Flask. Este contenedor está optimizado para una instalación mínima pero funcional.

### **Componentes Clave**:
1. **Imagen Base**:
   - Se utiliza `python:3.11-slim`, una imagen ligera que reduce el tamaño total del contenedor y acelera los tiempos de construcción.
2. **Instalación de Dependencias**:
   - Utiliza `Poetry` como gestor de dependencias, instalado mediante `pip`.
   - Las dependencias se instalan basándose en los archivos `pyproject.toml` y `poetry.lock` para garantizar un entorno reproducible.
3. **Copia del Código**:
   - Se seleccionan cuidadosamente solo los archivos necesarios (`app/`, `templates/`, `static/`, `tests/` y `.env`) para evitar archivos innecesarios en el contenedor.
4. **Exposición de Puertos**:
   - Expone el puerto `5000` para que la aplicación Flask sea accesible desde fuera del contenedor.
5. **Ejecución**:
   - La aplicación se ejecuta con el comando: `flask run --host=0.0.0.0 --port=5000`.

### **Uso**:
1. Construcción:
   ```bash
   docker build -t flask-web-app .
   ```
2. Ejecución:
   ```bash
   docker run -p 5000:5000 flask-web-app
   ```


## **2. Dockerfile para la API AIChronos**
### **Propósito**:
El Dockerfile para la API AIChronos configura un entorno ligero y eficiente para ejecutar la API basada en FastAPI.

### **Componentes Clave**:
1. **Imagen Base**:
   - Utiliza `python:3.11-slim`, por los mismos motivos que en el Dockerfile de la aplicación web.
2. **Instalación de Dependencias**:
   - Se instala `Poetry` mediante `pip` y luego se utilizan los archivos `pyproject.toml` y `poetry.lock` para instalar las dependencias requeridas.
3. **Copia del Código**:
   - Solo se copian los archivos esenciales, como el directorio `app/` que contiene la lógica de la API, `tests/` que contiene los tests de esta lógica y `.env` para configuraciones específicas del entorno.
4. **Exposición de Puertos**:
   - Expone el puerto `8000`, que es el puerto estándar para aplicaciones FastAPI utilizando `uvicorn`.
5. **Ejecución**:
   - La API se ejecuta mediante `uvicorn` con el comando: `uvicorn app.main:app --host 0.0.0.0 --port 8000`.

### **Uso**:
1. Construcción:
   ```bash
   docker build -t fastapi-api .
   ```
2. Ejecución:
   ```bash
   docker run -p 8000:8000 fastapi-api
   ```

## **Consideraciones Generales para Ambos Dockerfiles**
- **Optimización del Tamaño**:
  - Se elige una imagen base ligera (`slim`) para reducir los recursos necesarios.
- **Reproducibilidad**:
  - Al utilizar `pyproject.toml` y `poetry.lock`, se asegura que todas las dependencias sean consistentes entre los entornos.

## Documentación Adicional

1. [Documentación sobre el fichero de composición del clúster](compose.md)
2. [Documentación sobre la actualización, subida y publicación a Github Packages](github_packages.md)
3. [Descripición detallada de las imagenes base empleadas](github_packages.md)
4. [Inicio](../../README.md)