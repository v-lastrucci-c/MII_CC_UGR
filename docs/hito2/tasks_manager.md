# Comparativa de Task Managers

Los task managers son herramientas esenciales para automatizar y gestionar el flujo de trabajo, especialmente cuando hay múltiples tareas repetitivas como la ejecucuón de los tests. En este análisis compararemos tres herramientas: **Make**, **Invoke** y **Taskipy**.


## 1. Make

### Descripción
[Make](https://www.gnu.org/software/make/manual/make.html#Variables-Simplify) es una herramienta de automatización tradicional, originaria de los sistemas Unix. Se utiliza principalmente para gestionar compilaciones, pero su flexibilidad le permite manejar cualquier tipo de tarea.

### Características
- **Compatibilidad amplia**: Se encuentra en casi todos los sistemas Unix de forma nativa.
- **Control de dependencias**: Permite definir dependencias entre tareas fácilmente.
- **Versatilidad**: Aunque es ampliamente usado para compilación, puedes definir tareas personalizadas.

## 2. Invoke

### Descripción
[Invoke](https://www.pyinvoke.org/) es una librería en Python para gestionar tareas y comandos. Al utilizar Python, nos permite escribir tareas más complejas con lógica avanzada de una manera más legible.

### Características
- **Fácil de leer y mantener**: La sintaxis en Python hace que las tareas sean claras y fáciles de entender.
- **Interfaz de línea de comandos intuitiva**: Facilita el uso y la configuración de tareas.


## 3. Taskipy

### Descripción
[Taskipy](https://github.com/taskipy/taskipy) es una herramienta de gestión de tareas inspirado en el paquete [npm-run-script](https://docs.npmjs.com/cli/v10/commands/npm-run-script) de `npm`. Esta herramienta aprovecha la el archivo `pyproject.toml` para definir las tareas a ejecutar, por lo que fuerza a definir este archivo en el proyecto siguiendo las buenas prácticas [PEP 518](https://peps.python.org/pep-0518/).

### Características
- **Tareas en `pyproject.toml`**: Define tareas en `pyproject.toml`, manteniendo comandos de desarrollo organizados en un solo archivo.

- **Ejecución Simple**: Ejecuta cualquier tarea con `task <nombre>` o `poetry run task <nombre>`, simplificando el flujo de trabajo.

- **Comandos Flexibles**: Ejecuta cualquier comando de shell, permitiendo tareas de prueba, linting, construcción sin restricciones.

## Conclusión
Teniendo en cuenta las distintas opciones se ha optado por elegir **Taskipy** porque ya empleamos poetry como gestor de las dependencias del proyecto y porque su simpleza a la hora de definir las tareas que necesitamos es abrumadora. 

## Documentación Adicional
1. [Librería de Aserciones](assertion_library.md)
2. [Marco de Pruebas](testing_framework.md)
3. [Gestor de Integración Continua](continous_integration.md)
4. [Configuración de la Integración Continua](../hito2.md)
5. [Uso del Repo](repo_usage.md)
6. [Inicio](../README.md)
