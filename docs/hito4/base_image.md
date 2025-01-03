# Configuración de los Contenedores

Para realizar el desarrollo de los Dockerfiles se ha realizado un estudio de las imagenes base más apropiadas. Por un lado, debido a que los microservicios principales están desarrollados en `python`, se ha llevado a cabo la comparativa de las tres imagenes de python oficiales más apropiadas:

### 1. `python:3.11-slim`
   - **Tamaño**: Más ligera que la imagen completa de Python (~23 MB comprimido).
   - **Ventajas**:
     - Menor tamaño de imagen, lo que reduce los tiempos de construcción y despliegue.
     - Contiene solo los elementos esenciales para ejecutar Python.
     - Ideal para aplicaciones en producción donde se busca minimizar recursos.
   - **Desventajas**:
     - Puede requerir instalación manual de herramientas adicionales, como `curl`, `build-essential`, etc.
   - **Recomendación**:
     - Ideal para entornos controlados donde el objetivo principal es optimizar tamaño y velocidad.

### 2. `python:3.11`
   - **Tamaño**: Completa (~130 MB comprimido).
   - **Ventajas**:
     - Incluye herramientas adicionales preinstaladas como `gcc` y `git`, lo que simplifica el proceso de instalación de dependencias.
     - Menos configuraciones necesarias para entornos de desarrollo.
   - **Desventajas**:
     - Imagen significativamente más pesada.
     - Menor eficiencia en términos de uso de espacio en contenedores de producción.
   - **Recomendación**:
     - Adecuada para entornos de desarrollo o cuando necesitas compilar paquetes pesados.

### 3. `alpine:3.18` (con Python instalado)
   - **Tamaño**: Ultra ligera (~5 MB comprimido).
   - **Ventajas**:
     - Muy ligera, lo que reduce drásticamente el tamaño de la imagen.
     - Buena opción para entornos donde se desea máxima eficiencia.
   - **Desventajas**:
     - Puede ser complicado configurar dependencias que requieren compilación nativa.
     - No es oficialmente mantenida con un Python preinstalado, lo que implica configuraciones adicionales.
     - Algunas bibliotecas Python pueden no ser compatibles sin modificaciones.
   - **Recomendación**:
     - Ideal para proyectos avanzados donde el tamaño de la imagen sea crucial y haya experiencia con Alpine.

## Comparativa General

| Característica            | `python:3.11-slim`      | `python:3.11`        | `alpine:3.18`        |
|---------------------------|-------------------------|-----------------------|-----------------------|
| **Tamaño**                | ~23 MB                 | ~130 MB              | ~5 MB                |
| **Facilidad de Configuración** | Moderada                | Alta                  | Baja                 |
| **Velocidad de Construcción** | Alta                   | Media                 | Alta                 |
| **Compatibilidad de Paquetes** | Alta                   | Alta                  | Media                |
| **Uso Recomendada**       | Producción optimizada  | Desarrollo o general | Producción ligera    |

---

### **Conclusión**
- **`python:3.11-slim`** es la mejor opción para un equilibrio entre facilidad de uso y eficiencia, especialmente en producción.
- **`python:3.11`** es ideal para entornos de desarrollo o para proyectos que requieren herramientas adicionales preinstaladas.
- **`alpine:3.18`** es adecuada para usuarios avanzados con experiencia optimizando imágenes y necesidades de contenedores ultraligeros.

## Documentación Adicional
1. [Documentación sobre los Dockerfiles de los Microservicios](dockerfiles.md)
2. [Documentación sobre el fichero de composición del clúster](compose.md)
3. [Documentación sobre la actualización, subida y publicación a Github Packages](github_packages.md)
5. [Inicio](../../README.md)