import pytest
from app.internal.db import engine
from app.internal.models import Base

@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    # Crear tablas antes de la prueba
    Base.metadata.create_all(engine)
    yield
    # Eliminar tablas después de la prueba
    Base.metadata.drop_all(engine)
