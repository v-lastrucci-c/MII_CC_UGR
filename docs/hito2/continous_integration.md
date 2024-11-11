# Comparativa de Gestores de Integración Continua

Aquí realizaremos una comparación de tres de los gestores de integración continua (CI) más utilizados: **Jenkins**, **Travis** y **GitHub Actions**.


## Jenkins

- **Extensibilidad**: Cuenta con una gran cantidad de plugins que permiten adaptarse a casi cualquier flujo de trabajo que necesite integrar un pipeline de CI/CD.
- **Escalabilidad**: Jenkins permite la configuración de múltiples nodos y agentes, lo cual es ideal para proyectos de gran escala.
- **Comunidad y soporte**: Al ser uno de los sistemas CI más antiguos cuenta con una gran comunidad de usuarios junto con una documentación extensa.

## Travis CI

- **Facilidad de configuración**: Se configura con un simple archivo `.travis.yml` en el repositorio.
- **Integración con GitHub**: Se integra muy bien con GitHub, permitiendo un flujo de trabajo directo con esta plataforma.
- **Compatibilidad con múltiples lenguajes**: Soporta múltiples lenguajes de programación y entornos.

## GitHub Actions

- **Integración nativa con GitHub**: Al estar desarrollado por GitHub se integra directamente con sus repositorios.
- **Flexibilidad y personalización**: Se pueden definir los flujos de trabajo usando `YAML` para personalizar y configurar cada etapa de CI/CD.
- **Gran cantidad de acciones reutilizables**: Existe una gran cantidad de acciones prediseñadas, permitiendo la creación de flujos de trabajo o adición de etapas sin necesidad de desarrollar cada paso desde cero.


## Conclusión

Elegiremos **GitHub Actions** como sistema de integración continúa por su gran cantidad de acciones reutilizables y por su sencilla y clara configuración en un archivo `.yaml`.

## Documentación Adicional
1. [Librería de Aserciones](assertion_library.md)
2. [Marco de Pruebas](testing_framework.md)
3. [Gestor de Tareas](tasks_manager.md)
4. [Configuración de la Integración Continua](../hito2.md)
5. [Uso del Repo](repo_usage.md)
6. [Inicio](../README.md)