# Documentación del compose.yml

El archivo `compose.yml` define el clúster de contenedores para la aplicación **AIChronos**, compuesto por tres servicios principales: `aichronos-web`, `aichronos-api` y `aichronos-db`.

## Servicios

### 1. **aichronos-web**
Servicio que gestiona el frontend de la aplicación.

- **Build:**
  - Contexto: `./src/web`
  - Dockerfile: `Dockerfile`
- **Nombre del contenedor:** `aichronos-web`
- **Imagen:** `ghcr.io/v-lastrucci-c/mii_cc_ugr-web:latest`
- **Puertos:**
  - Expuesto: `5000`
  - Mapeado a: `5000` en el host
- **Variables de entorno:** Cargadas desde `./src/web/.env_production`
- **Dependencias:** Este servicio depende de:
  - `aichronos-api`
  - `aichronos-db`
- **Comando:**
  Ejecuta la inicialización de la base de datos y arranca el servidor Flask:
  ```bash
  sh -c "flask init-db && flask run --host=0.0.0.0 --port=5000"
  ```

### 2. **aichronos-api**
Servicio que gestiona el backend o API de la aplicación.

- **Build:**
  - Contexto: `./src/api`
  - Dockerfile: `Dockerfile`
- **Nombre del contenedor:** `aichronos-api`
- **Imagen:** `ghcr.io/v-lastrucci-c/mii_cc_ugr-api:latest`
- **Puertos:**
  - Expuesto: `8000`
  - Mapeado a: `8000` en el host
- **Variables de entorno:** Cargadas desde `./src/api/.env_production`


### 3. **aichronos-db**
Servicio que proporciona la base de datos para la aplicación.

- **Imagen:** `postgres:15`
- **Nombre del contenedor:** `aichronos-db`
- **Puertos:**
  - Expuesto: `5432`
  - Mapeado a: `5432` en el host
- **Entorno:**
  - Usuario: `aichronos`
  - Contraseña: `aichronos*`
  - Base de datos: `aichronos_db`
- **Volúmenes:**
  - Persistencia: Montado en `postgres_data:/var/lib/postgresql/data`


## Volúmenes

- **postgres_data:** Volumen nombrado para la persistencia de datos de la base de datos PostgreSQL.


## Dependencias entre Servicios

El servicio `aichronos-web` depende de:
- `aichronos-api`
- `aichronos-db`

Esto garantiza que ambos servicios estén disponibles antes de iniciar el frontend.

## Uso

1. **Construir los contenedores:**
   ```bash
   docker-compose build
   ```
2. **Iniciar el clúster:**
   ```bash
   docker-compose up
   ```
3. **Detener el clúster:**
   ```bash
   docker-compose down
   ```

## Notas

- Los archivos `.env_production` deben contener las variables de entorno necesarias para cada servicio, modifiquelas en caso necesario.

## Documentación Adicional

1. [Documentación sobre los Dockerfiles de los Microservicios](dockerfiles.md)
2. [Documentación sobre la actualización, subida y publicación a Github Packages](github_packages.md)
3. [Descripición detallada de las imagenes base empleadas](github_packages.md)
4. [Inicio](../../README.md)