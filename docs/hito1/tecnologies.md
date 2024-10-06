# Tecnologías Usadas y Comparativas

## Flask

**Por qué usar Flask como interfaz web para gestionar el acceso a los endpoints de FastAPI y registrar y logear al usuario:**

- **Ligereza y Flexibilidad:** Flask es un microframework minimalista que permite desarrollar aplicaciones web de manera rápida y sencilla.
- **Facilidad de Integración:** Se integra fácilmente con otras herramientas y bibliotecas, lo que lo hace ideal para proyectos que requieren personalización.
- **Comunidad Activa:** Cuenta con una gran comunidad y abundante documentación.

**Comparación con otras tecnologías:**

1. **Django:**
   - *Ventajas:*
     - Framework completo con muchas funcionalidades integradas.
     - Sistema de autenticación y administración listo para usar.
   - *Desventajas:*
     - Más pesado y con una curva de aprendizaje más pronunciada.
     - Puede ser excesivo para proyectos pequeños o medianos.

2. **Express.js (Node.js):**
   - *Ventajas:*
     - Gran rendimiento en aplicaciones en tiempo real.
     - Amplio ecosistema de paquetes a través de NPM.
   - *Desventajas:*
     - Menos adecuado si el resto del stack está en Python.

## PostgreSQL

**Por qué usar PostgreSQL para almacenar los usuarios registrados:**

- **Robustez y Fiabilidad:** PostgreSQL es conocido por su estabilidad y conformidad con estándares SQL.
- **Características Avanzadas:** Soporta transacciones complejas, extensiones y tipos de datos avanzados.
- **Seguridad:** Ofrece sólidas características de seguridad y control de acceso.

**Comparación con otras tecnologías:**

1. **MySQL:**
   - *Ventajas:*
     - Amplia adopción y comunidad.
     - Buen rendimiento en lecturas.
   - *Desventajas:*
     - Menos funciones avanzadas que PostgreSQL.
     - Históricamente menos estricto con los estándares SQL.

2. **MongoDB:**
   - *Ventajas:*
     - Modelo flexible de documentos NoSQL.
     - Escalabilidad horizontal sencilla.
   - *Desventajas:*
     - Menos adecuado para datos relacionales y transaccionales.
     - Falta de integridad referencial.

## FastAPI

**Por qué usar FastAPI para gestionar los endpoints de interacción con el LLM:**

- **Alto Rendimiento:** Basado en ASGI y construido sobre Starlette, ofrece un rendimiento superior y soporte para operaciones asíncronas.
- **Validación Automática:** Utiliza Pydantic para validar datos, lo que reduce errores.
- **Documentación Interactiva:** Genera automáticamente documentación Swagger y OpenAPI.

**Comparación con otras tecnologías:**

1. **Django REST Framework (DRF):**
   - *Ventajas:*
     - Integración completa con Django.
     - Muchas funcionalidades listas para usar.
   - *Desventajas:*
     - Menos rendimiento en aplicaciones asíncronas.
     - Mayor sobrecarga para configuraciones simples.

2. **Bottle:**
   - *Ventajas:*
     - Framework muy ligero y sencillo.
     - Fácil de aprender y usar.
   - *Desventajas:*
     - Menos funcionalidades integradas.
     - Comunidad y soporte más pequeños.

## LangGraph

**Por qué usar LangGraph para diseñar las llamadas del LLM:**

- **Diseño de Flujo Eficiente:** Permite crear y visualizar flujos complejos de interacción con modelos de lenguaje.
- **Modularidad:** Facilita la reutilización y mantenimiento de componentes en las llamadas al LLM.
- **Optimización:** Ayuda a optimizar el rendimiento y manejo de errores en las interacciones.

**Comparación con otras tecnologías:**

1. **Agency-Swarm:**
   - *Ventajas:*
     - Orientado a la coordinación de múltiples agentes de IA.
     - Facilita la creación de sistemas multiagente y colaboración entre ellos.
   - *Desventajas:*
     - Se basa en el [Assistants API](https://platform.openai.com/docs/assistants/overview) de OpenAI que se encuentra en estado __Beta__.

2. **Directamente usar la API del LLM:**
   - *Ventajas:*
     - Mayor control y personalización en las llamadas.
     - Evita dependencias adicionales.
   - *Desventajas:*
     - Requiere más código y manejo manual de flujos.
     - Mayor probabilidad de errores y dificultad en el mantenimiento.

---

Las tecnologías elegidas ofrecen un equilibrio entre funcionalidad, rendimiento y facilidad de uso, lo que las hace ideales para el desarrollo de esta aplicación que gestiona usuarios y utiliza modelos de lenguaje.

## Documentación Adicional
1. [Descripción detallada del proyecto](../hito1.md)
2. [Inicio](../../README.md)
