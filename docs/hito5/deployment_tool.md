# Descripción y Justificación del Despliegue en Render utilizando Blueprints

El archivo [`render.yaml`](../../render.yaml) centraliza la configuración de todos los servicios necesarios para la aplicación, incluyendo el frontend, backend y la base de datos. A continuación, se detallan estos componentes:

## 1. Servicio Web (Frontend)

- **Configuración:**
  - Servicio de tipo `web` denominado `MII_CC_UGR_WEB`.
  - Implementación mediante Docker, especificando `dockerContext`, `dockerfilePath` y `rootDir`.
  - Repositorio en GitHub para integración continua.
  - Variables de entorno como `SQLALCHEMY_DATABASE_URI`, `SECRET_KEY` y `DEBUG`.
  - Región: `frankfurt` (Europa).

**Justificación:**

La utilización de Docker garantiza un entorno de ejecución consistente y reproducible, independientemente del entorno físico. La integración con GitHub permite despliegues automáticos y control de versiones eficiente. Las variables de entorno facilitan la configuración dinámica y segura de parámetros sensibles. La elección de la región `frankfurt` asegura el cumplimiento de normativas europeas de protección de datos y optimiza la latencia para los usuarios en Europa.

## 2. Servicio API (Backend)

- **Configuración:**
  - Servicio de tipo `web` denominado `MII_CC_UGR_API`.
  - Implementación mediante Docker, con especificaciones similares al frontend.
  - Repositorio en GitHub para integración continua.
  - Variables de entorno como `DATABASE_URL` y `OPENAI_API_KEY`.
  - Región: `frankfurt` (Europa).

**Justificación:**

La separación del backend como un servicio independiente mejora la escalabilidad y el mantenimiento de la aplicación. Docker asegura que el entorno de ejecución sea coherente con el del frontend, facilitando la integración y el despliegue. Las variables de entorno permiten gestionar de forma segura las credenciales y configuraciones necesarias para la interacción con servicios externos. La ubicación en `frankfurt` garantiza el cumplimiento de las regulaciones europeas y mejora la experiencia del usuario en la región.

## 3. Base de Datos

- **Configuración:**
  - Base de datos PostgreSQL denominada `MII_CC_UGR_DB`.
  - Nombre de la base de datos: `aichronos_db`.
  - Usuario: `aichronos`.
  - Plan gratuito y lista de IPs permitidas amplia (`0.0.0.0/0`).
  - Versión de PostgreSQL: 15.
  - Región: `frankfurt` (Europa).

**Justificación:**

PostgreSQL es una base de datos relacional robusta y confiable, adecuada para aplicaciones que requieren una gestión eficiente de datos. La configuración declarativa en el `render.yaml` permite una fácil reproducción del entorno de base de datos. La región `frankfurt` asegura que los datos se almacenen conforme a las leyes europeas de protección de datos y proporciona una baja latencia para los usuarios locales.

## Conclusión

La implementación de **Infrastructure as Code** mediante el archivo `render.yaml` en Render nos permite definir y gestionar la infraestructura de la aplicación de manera declarativa y reproducible. Esta práctica mejora la consistencia entre entornos, facilita el control de versiones y simplifica el proceso de despliegue. La elección de Docker como entorno de ejecución y PostgreSQL como sistema de gestión de bases de datos proporciona una base sólida y escalable para la aplicación, mientras que la ubicación en la región `frankfurt` garantiza el cumplimiento de las normativas europeas y una óptima experiencia de usuario.

## Documentación Adicional

1. [Documentación sobre la comparativa entre los PaaS](./paas_selection.md)
2. [Documentación sobre el despliegue automatizado mediante GitHub Acitons](./deploy_githubActions.md)
3. [Despliegue automático al PaaS](../hito5.md)
4. [Inicio](../../README.md)