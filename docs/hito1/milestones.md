# Milestones
1. Planificación y Diseño Inicial
    - Configurar el repositorio de código (GitHub).
    - Seleccionar las tecnologías y herramientas a utilizar.
    - Definir los requisitos del agente.

2. Configuración del Entorno de Desarrollo e Integración Continua
    - Implementar la pipeline de CI utilizando herramientas como GitHub Actions o Jenkins.
    - Configurar entornos de desarrollo para Flask, FastAPI y PostgreSQL.

3. Desarrollo de Microservicio de FastAPI
    - Implementar los endpoints en FastAPI con los que se interactuará con el modelo.
    - Configurar la base de datos PostgreSQL para almacenar usuarios y contraseñas.

4. Desarrollo de la Interfaz Web con Flask
    - Configurar el proyecto Flask.
    - Implementar el microservicio de autenticación y gestión de usuarios con Flask.
    - Desarrollar las páginas de registro, inicio de sesión y recuperación de contraseña.
    - Integrar los endpoints de FastAPI en la interfaz web.

5. Integración con LangGraph y Funcionalidades del Agente
    - Configurar y diseñar el grafo de conocimiento con LangGraph.
    - Desarrollar la lógica de interacción del agente dentro de FastAPI.
    - (Opcional) Desarrollar herramienta para crear eventos en Google Calendar.

6. Despliegue y Monitoreo
    - Establecer pruebas automatizadas básicas (unitarias).
    - Contenerizar las aplicaciones Flask, FastAPI y la base de datos usando Docker.
    - Desplegar los microservicios en la plataforma PaaS seleccionada.
    - Configurar herramientas de logging y Monitoreo.

## Documentación Adicional
1. [Historias de Usuario](hu.md)
2. [Configuración del Repositorio](config_repo.md)
3. [Descripción detallada del proyecto](../hito1.md)
4. [Inicio](../../README.md)
