# Requisitos Previos

Versión de Python 3.11 o superior.

## 1. Crear un Entorno Virtual

Crear y activar un entorno virtual con los siguientes comandos:

```bash
python -m venv .venv
.venv\Scripts\activate   Windows
```

## 2. Instalar Poetry

[Poetry](https://python-poetry.org/) es un gestor de dependencias y entorno para proyectos de Python. Para instalar Poetry, ejecuta el siguiente comando:

```bash
pip install poetry
```

## 3. Instalar Dependencias

Ubicarnos en el directorio de ambas aplicaciones,
```bash
cd src/api # cd src/web
```
Instalar las dependencias con el siguiente comando,

```bash
poetry install
```

Este comando instalará todas las dependencias listadas en `pyproject.toml`.

## 4. Configurar Variables de Entorno
Crear un archivo `.env` en el directorio de `web` para almacenar las variables de entorno necesarias:

```text
SECRET_KEY = Clave para la seguridad de Flask.
SQLALCHEMY_DATABASE_URI = URI para conectar la base de datos.
DB_USER = Usuario de la base de datos.
DB_PASSWORD = Contraseña de la base de datos.
DB_HOST = Dirección del servidor de la base de datos.
DB_PORT = Puerto del servidor de la base de datos.
DB_NAME = Nombre de la base de datos.
FLASK_DEBUG = Activa el modo de depuración en Flask.
SQLALCHEMY_TRACK_MODIFICATIONS = Control de cambios en SQLAlchemy.
DEBUG = Habilita mensajes de depuración.
PORT = Puerto de la aplicación Flask.
TESTING = Activa el modo de pruebas en Flask
```

## 5. Iniciar la API
Para iniciar la `api` deberemos ubicarnos en el directorio `src/api` y ejecutar el siguiente comando:
```bash
fastapi dev app/main.py
```

Una vez iniciada, podemos ver la documentación de la API visitando [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## 6. Iniciar la Aplicación

Para iniciar la aplicación `web`, primero debemos crear las tablas correspondientes en PostgreSQL mediante el siguiente comando:

```bash
flask --app app init-db
```
Luego podemos proceder a ejecutar la aplicación,
```bash
flask --app app run
```

Esto iniciará la aplicación en `http://127.0.0.1:5000/` o en el puerto especificado en las variables de entorno.

## 7. Ejecutar Pruebas
Para ejecutar las pruebas de ambos servicios haremos uso del task manager configurado, lo que tendremos que hacer es ubicarnos en los directorios de `api` y `web` respectivamente y ejecutar el siguiente comando:

```bash
poetry run task test
```

Una vez finalizados los tests podemos ver el informe de coverage generado accediendo a la carpeta [src\api\htmlcov](../src/api/htmlcov/) y abriendo el archivo `index.html` en el navegador.

## Documentación Adicional
1. [Librería de Aserciones](assertion_library.md)
2. [Marco de Pruebas](testing_framework.md)
3. [Gestor de Tareas](tasks_manager.md)
4. [Gestor de Integración Continua](continous_integration.md)
5. [Configuración de la Integración Continua](../hito2.md)
6. [Inicio](../README.md)