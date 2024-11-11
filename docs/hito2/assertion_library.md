# Comparativa de Bibliotecas de Aserciones

## Introducción

Aunque Python incluye la biblioteca estándar `unittest` para realizar pruebas, existen otras opciones que ofrecen funcionalidades adicionales o más intuitivas. En este documento compararemos tres bibliotecas de aserciones para el testeo en Python: **Pytest**, **Unittest** y **Behave**. También justificaremos la elección del estilo de pruebas utilizado, confrontando **TDD (Desarrollo Dirigido por Pruebas)** y **BDD (Desarrollo Dirigido por Comportamiento)**.


## Comparativa de Bibliotecas

### 1. Pytest

#### Descripción

[Pytest](https://docs.pytest.org/) es una biblioteca de pruebas que simplifica la escritura y ejecución de los tests. Ofrece una sintaxis intuitiva permitiendo crear pruebas más concisas y legibles.

#### Ventajas

- **Sintaxis más sencilla y legible**: Utiliza una sintaxis más simple y legible que Unittest. No es necesario escribir clases y métodos para cada prueba, solo necesitas funciones y afirmaciones simples (`asserts`).
- **Fixtures Flexibles**: Proporciona un sistema flexible de fixtures para manejar configuraciones y datos de prueba reutilizables.
- **Parametrización**: Ofrece una forma sencilla y potente de parametrizar las pruebas, lo que te permite probar diferentes entradas y salidas con el mismo código.
- **Amplia Extensibilidad**: Cuenta con una variedad de plugins que extienden su funcionalidad, como `pytest-cov` para la cobertura de código.

#### Estilo

Se alinea principalmente con el **TDD**, facilitando la escritura de pruebas unitarias y fomentando el desarrollo incremental basado en pruebas.


### 2. Unittest

#### Descripción

[Unittest](https://docs.python.org/3/library/unittest.html) es la biblioteca de pruebas estándar incluida en Python, inspirada en JUnit para Java. Utiliza un estilo orientado a clases para organizar y ejecutar pruebas.

#### Ventajas

- **Estándar Incorporado**: Al estar incluida en la biblioteca estándar de Python, no requiere instalaciones adicionales.
- **Estructura basada en clases**: Utiliza clases y métodos específicos (`TestCase`, `setUp`, `tearDown`) que han de heredar de `unittest.TestCase`, añadiendo algo de verbosidad y complejidad.
- **Métodos de Aserción Específicos**: Ofrece una amplia gama de métodos de aserción (`assertEqual`, `assertTrue`, `assertRaises`, etc.) para comparar resultados esperados y obtenidos.


#### Estilo

También se asocia con el **TDD**, pero su enfoque es más tradicional y estructurado que **Pytest**.


### 3. Behave

#### Descripción

[Behave](https://behave.readthedocs.io/en/latest/) es una biblioteca que implementa el estilo BDD, permitiendo escribir pruebas basadas en el comportamiento usando lenguaje natural a través de Gherkin.

#### Ventajas

- **Lenguaje Natural**: Permite escribir escenarios de prueba en lenguaje natural (`Given`, `When`, `Then`), facilitando la comprensión por parte de agentes no técnicos.
- **Estructura Orientada al Comportamiento**: Organiza las pruebas en características y escenarios centrados en el comportamiento y requisitos del usuario.
- **Aserciones Claras**: Las aserciones se integran dentro de los pasos definidos, permitiendo comparaciones claras entre resultados esperados y obtenidos.

#### Estilo

Está diseñado específicamente para **BDD**, enfocándose en describir el comportamiento del sistema desde la perspectiva del usuario final.


## Comparativa entre TDD y BDD

### Desarrollo Dirigido por Pruebas (TDD)

#### Enfoque

Escribir pruebas unitarias **antes** del código funcional, asegurando que cada unidad de código cumple con su especificación.

#### Beneficios

- **Calidad del Código**: Promueve un diseño de código limpio y modular.
- **Detección Temprana de Errores**: Identifica problemas en etapas iniciales del desarrollo.
- **Refactorización Segura**: Facilita cambios en el código verificando su funcionalidad gracias al suite de pruebas previamente desarrollado.

### Desarrollo Dirigido por Comportamiento (BDD)

#### Enfoque

Centrado en el comportamiento del sistema y la satisfacción de los requisitos del usuario, utilizando un lenguaje común para describir las pruebas.

#### Beneficios

- **Comunicación Efectiva**: Mejora la colaboración entre equipos técnicos y no técnicos.
- **Alineación con el Negocio**: Asegura que el desarrollo está alineado con los objetivos y necesidades del negocio.
- **Documentación Viva**: Las pruebas sirven como documentación actualizada del comportamiento del sistema.

## Elección del Estilo

Como este proyecto carece de un equipo no técnico, considero que es más conveniente asegurar la calidad interna del código, facilitando un desarrollo ágil y orientado a pruebas. Por lo tanto el estilo elegido para el desarrollo de las pruebas será **TDD**.

Entre las librerías comparadas se han comentado dos que servirían para este estilo, **Pytest** y **Unittest**. Nos decantaremos por `Pytest` debido a su sintaxis, por los elementos `fixtures` y por la posibilidad de parametrizar las pruebas de manera sencilla.


## Documentación Adicional
1. [Marco de Pruebas](testing_framework.md)
2. [Gestor de Tareas](tasks_manager.md)
3. [Gestor de Integración Continua](continous_integration.md)
4. [Configuración de la Integración Continua](../hito2.md)
6. [Uso del Repo](repo_usage.md)
5. [Inicio](../README.md)