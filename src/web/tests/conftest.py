import sys
import os

# Añadir la carpeta web al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app, db
from app.models import User


# Configuración de prueba
@pytest.fixture
def app():
    # Crear la aplicación en modo de prueba
    os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SECRET_KEY": "test",
        "SERVER_NAME": "localhost",
    })

    # Crear la base de datos y el esquema
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    # Asegurar que el cliente se use dentro de un contexto de solicitud
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

# Fixture para crear un usuario de prueba
@pytest.fixture
def user(app):
    with app.app_context():
        user = User(name="testuser", email="test@example.com")
        user.set_password("mysecretpassword")
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)  # Asegurar que el objeto esté enlazado a la sesión
        return user
