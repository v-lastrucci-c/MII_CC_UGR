# Comparativa de Librerías de Logging

A continuación, presentaremos una comparativa de las tres principales librerías de logging en Python:

## 1. Módulo Estándar de Logging

- **Integración Nativa**: Incluido en la biblioteca estándar de Python, permite iniciar el registro sin configuraciones adicionales.
- **Niveles de Severidad**: Soporta niveles como DEBUG, INFO, WARNING, ERROR y CRITICAL, facilitando la categorización de mensajes según su importancia.
- **Personalización**: Ofrece clases como `Handler`, `Formatter` y `Filter` para definir destinos de salida, formatos de registro y filtros personalizados.

## 2. Loguru

- **Facilidad de Uso**: Simplifica el proceso de logging con una configuración mínima, permitiendo iniciar registros con solo importar el módulo.
- **Salida Personalizable**: Permite configurar destinos de salida, niveles de registro y formatos, incluyendo opciones para serializar registros en JSON.
- **Manejo de Excepciones**: Ofrece herramientas integradas para capturar y registrar excepciones de manera detallada.

## 3. Structlog

- **Logging Estructurado**: Facilita la creación de registros estructurados, mejorando la legibilidad y el análisis automatizado.
- **Integración con Asyncio**: Soporta aplicaciones asíncronas, adaptándose a entornos modernos de desarrollo.
- **Compatibilidad**: Se integra fácilmente con el módulo estándar de logging de Python, permitiendo una transición sin problemas.

## Elección de Loguru

Se ha optado por **Loguru** debido a las siguientes razones:

- **Simplicidad y Eficiencia**: Su API intuitiva reduce la complejidad en la configuración y uso del logging.
- **Flexibilidad**: La capacidad de personalizar formatos y destinos de registro se adapta a diversas necesidades del proyecto.
- **Manejo Avanzado de Excepciones**: Proporciona herramientas que facilitan la captura y registro detallado de excepciones, mejorando la depuración.

## Documentación Adicional
1. [Justificación técnica del framework elegido para la API](../hito1/tecnologies.md)
2. [Diseño de microservicios](../hito3.md)
3. [Inicio](../README.md)
