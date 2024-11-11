# Comparación de Test Runners

### Introducción
Los mismos frameworks de pruebas `Pytest`, `Unittest` y `Behave` que hemos analizado en la [Comparación de Librerías de Asserciones](./assertion_library.md) permiten ejecutar y gestionar pruebas como test runners.

## Pytest
Si nos ubicamos en la carpeta `web` por ejemplo, podríamos utilizar **Pytest** como test runner ejecutando solamente el siguiente comando:

```bash
pytest
```

**Pytest** buscará automáticamente los archivos y funciones de prueba que sigan las convenciones de nombres (`test_`). Además, es posible instalar **pytest-cov**, un complemento que permite medir la cobertura de código durante la ejecución de las pruebas.

### Medición de Cobertura con Pytest-cov
Para generar un informe en formato, por ejemplo `html`, de la cobertura, es tan sencillo como ejecutar **Pytest** con la opción `--cov`:

```bash
pytest --cov=app --cov-report=html --cov-report=xml tests\test_flask_app.py
```

El documento generado se encuentra en la carpeta [htmlcov](../../src/web/htmlcov/), donde, abriendo el index.html en un navegador, se puede ver el coverage.

## Ejecución de Unittest
Para usar **Unittest** como test runner, se puede ejecutar el módulo `unittest` directamente:

```bash
python -m unittest discover
```

Este comando descubrirá y ejecutará todas las pruebas organizadas en clases dentro del proyecto.

## Ejecución de Behave como Test Runner
Para ejecutar pruebas con **Behave** se utiliza el siguiente comando:

```bash
behave
```

Behave interpretará los archivos `.feature`, escritos en lenguaje natural, siguiendo el estilo BDD. Los steps, definidos en el código Python, se enlazan con los pasos en estos archivos `.feature`.

## Elección de Test Runner
Para ser coherentes con la elección de la librería de aserción, vamos a hacer uso del test runner **Pytest**.

## Documentación Adicional
1. [Librería de Aserciones](assertion_library.md)
2. [Gestor de Tareas](tasks_manager.md)
3. [Gestor de Integración Continua](continous_integration.md)
4. [Configuración de la Integración Continua](../hito2.md)
5. [Uso del Repo](repo_usage.md)
6. [Inicio](../README.md)