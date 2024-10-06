# Descripción del proyecto
El proyecto consistirá en un agente inteligente desarrollado en Python aprovechando el framework de LangGraph, ofreciendo una interfaz web intuitiva mediante Flask y gestionando las peticiones API con FastAPI.

Permitirá a los usuarios registrarse, iniciar sesión y recuperar sus contraseñas de manera segura, almacenando sus datos en una base de datos PostgreSQL.

El agente será desarrollado mediante LangGraph para acceder y actualizar grafos de conocimiento, proporcionando respuestas precisas y contextualizadas. Además, los usuarios podrán crear eventos a través de integraciones con herramientas externas como Google Calendar.

El sistema garantizará la seguridad de los datos mediante encriptación de contraseñas y contará con monitoreo y logging para asegurar un rendimiento óptimo y facilitar la detección de problemas. Todo esto se desplegará en una plataforma PaaS todavía por determinar, asegurando escalabilidad y facilidad de mantenimiento.

Para más información sobre la elección de las teconologías empleadas clique [aquí](./hito1/tecnologies.md).


## **Tipos de Clientes**
| **Clase de Cliente** | **Descripción** | **Principales Funcionalidades** |
|----------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Usuarios Finales** | Usuarios comunes que interactúan con el agente. | - Registro y autenticación.<br>- Interacción con el agente.<br>- Uso de herramientas integradas.|
| **Administradores**  | Usuarios con permisos elevados para gestionar el sistema. | - Gestión de usuarios.<br>- Monitoreo y generación de reportes.<br>- Supervisión del sistema.|


## Documentación Adicional
1. [Milestones](./hito1/milestones.md)
2. [Historias de Usuario](./hito1/hu.md)
3. [Configuración del Repositorio](./hito1/config_repo.md)
4. [Inicio](../README.md)
