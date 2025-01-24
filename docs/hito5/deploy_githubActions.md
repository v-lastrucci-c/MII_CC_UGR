# Descripción de la Configuración para el Despliegue Automático al PaaS desde el Repositorio de GitHub

Para desarrollar el despliegue automático al PaaS **Render** desde el repositorio de GitHub hemos utilizado un flujo de trabajo configurado mediante **GitHub Actions**. Este flujo de trabajo permite desplegar los servicios definidos (API y Web) automáticamente al realizar cambios en la rama principal (`main`) o manualmente a través de la opción `workflow_dispatch`. A continuación, se describe cada componente de la configuración:

## 1. Evento que Dispara el Flujo de Trabajo
El flujo de trabajo se activa en las siguientes situaciones:
- **Push a la Rama Principal (`main`)**: Cualquier cambio que se suba a esta rama ejecutará el despliegue.
- **Ejecución Manual (`workflow_dispatch`)**: El flujo puede iniciarse manualmente desde la interfaz de GitHub Actions.


## 2. Instalación y Autenticación
- **Acceso al Código del Repositorio:**
  - La acción `actions/checkout@v4` descarga el código fuente del repositorio para habilitar cualquier proceso adicional que dependa de este.
- **Autenticación con Render:**
  - Se utiliza la acción personalizada `JorgeLNJunior/render-deploy`, que requiere:
    - Una clave de API de Render (`RENDER_API_KEY`).
    - Identificadores únicos (`service_id`) para cada servicio que se despliega.
  - Las claves y configuraciones sensibles se gestionan mediante **GitHub Secrets**, garantizando la seguridad.


## 3. Servicios a Desplegar
El flujo de trabajo está diseñado para desplegar los siguientes servicios:

### 3.1. API
- **Configuración:**
  - Identificado por `RENDER_API_SERVICE_ID`.
  - El despliegue incluye la opción `wait_deploy: true`, que garantiza que el proceso espere hasta que Render complete el despliegue del servicio antes de continuar.

### 3.2. Web
- **Configuración:**
  - Identificado por `RENDER_WEB_SERVICE_ID`.
  - Configuración similar a la del servicio API, asegurando que el despliegue del frontend sea confiable y sincronizado.

### **5. Ventajas de la Configuración**
- **Automatización Total:** El despliegue se ejecuta automáticamente con cada cambio en la rama principal, reduciendo el riesgo de errores manuales.
- **Despliegue Modular:** Permite gestionar el backend (API) y el frontend (Web) de forma independiente.
- **Sincronización Asegurada:** La opción `wait_deploy: true` evita que se solapen despliegues, asegurando que cada servicio se despliegue correctamente antes de proceder al siguiente.
- **Seguridad:** Las claves y configuraciones sensibles se almacenan en **GitHub Secrets**, minimizando riesgos de exposición.

---

### **6. Ejemplo del Flujo de Trabajo**
A continuación, incluimos el flujo de trabajo completo utilizado para la configuración descrita:

```yaml
name: Deploy AIChronos to Render

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    name: Deploy AIChronos to Render
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Deploy API to production
        uses: JorgeLNJunior/render-deploy@v1.4.4
        with:
          service_id: ${{ secrets.RENDER_API_SERVICE_ID }}
          api_key: ${{ secrets.RENDER_API_KEY }}
          wait_deploy: true
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Deploy WEB to production
        uses: JorgeLNJunior/render-deploy@v1.4.4
        with:
          service_id: ${{ secrets.RENDER_WEB_SERVICE_ID }}
          api_key: ${{ secrets.RENDER_API_KEY }}
          wait_deploy: true
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

## Documentación Adicional

1. [Documentación sobre la comparativa entre los PaaS](./paas_selection.md)
2. [Documentación sobre la herramienta de despliegue Render](./deployment_tool.md)
3. [Despliegue automático al PaaS](../hito5.md)
4. [Inicio](../../README.md)