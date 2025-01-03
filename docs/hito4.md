# Despliegue de los Microservicios

## Estructura del clúster de contenedores

El clúster de contenedores está compuesto por tres servicios principales que se gestionan a través del archivo `compose.yml`:

1. **aichronos-web:** Servicio que gestiona el frontend de la aplicación.
2. **aichronos-api:** Servicio que implementa la API de backend.
3. **aichronos-db:** Servicio que proporciona la base de datos PostgreSQL para la aplicación.

Todos los servicios están interconectados y definidos en el archivo de composición, asegurando que las dependencias sean resueltas automáticamente.

Para más detalles, consulta la [Documentación del compose.yml](./hito4/compose.md).


## Configuración de los contenedores

Los microservicios están configurados usando Dockerfiles optimizados para entornos de desarrollo y producción. Se han tomado decisiones estratégicas sobre las imágenes base:

1. **Frontend y Backend:** Utilizan `python:3.11-slim` para reducir el tamaño de las imágenes y mejorar la velocidad de construcción.
2. **Base de Datos:** Se emplea la imagen oficial `postgres:15` para garantizar estabilidad y rendimiento.

### Justificación del uso de `postgres:15`

Se utiliza la imagen oficial `postgres:15` en lugar de otras alternativas debido a:

1. **`postgres:alpine`**
   - **Ventajas:**
     - Imagen extremadamente ligera (~5 MB comprimido), ideal para entornos donde el tamaño de la imagen es crítico.
   - **Desventajas:**
     - Mayor complejidad al configurar extensiones o dependencias que requieren compilación nativa.
     - Menor compatibilidad con herramientas avanzadas y librerías debido a su enfoque minimalista.

2. **`postgres:latest`**
   - **Ventajas:**
     - Garantiza siempre la última versión estable, sin necesidad de actualizar manualmente.
     - Buena compatibilidad con herramientas y configuraciones estándar.
   - **Desventajas:**
     - Puede causar problemas de compatibilidad con entornos ya desplegados si la versión cambia inesperadamente.

**Decisión:** Se elige `postgres:15` porque combina estabilidad (versión fija), características modernas y facilidad de uso, a la vez que evita los problemas de tamaño de `postgres:alpine` y la incertidumbre de actualizaciones automáticas de `postgres:latest`.

## Ejecución del test para validar el funcionamiento del cluster

## Documentación Adicional

1. [Documentación sobre los Dockerfiles de los Microservicios](./hito4/dockerfiles.md)
2. [Documentación sobre el fichero de composición del clúster](./hito4/compose.md)
3. [Documentación sobre la actualización, subida y publicación a Github Packages](./hito4/github_packages.md)
4. [Descripición detallada de las imágenes base empleadas](./hito4/base_image.md)
5. [Inicio](../README.md)
