from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_app_initialization():
    """
    Verifica que la aplicación se inicializa correctamente con los detalles básicos.
    """
    assert app.title == "API AICHRONOS"
    assert app.version == "1.0.0"

def test_cors_configuration():
    """
    Verifica que CORS está configurado correctamente con una ruta válida.
    """
    response = client.get("/api/v1/health", headers={"Origin": "http://localhost"})
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == "http://localhost"

def test_get_user_profile_not_found(mocker):
    # Crear un mock para el objeto `session`
    mock_session = mocker.patch("app.routers.profile.session", autospec=True)

    # Configurar el mock para que `query` devuelva un resultado filtrado nulo
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value.first.return_value = None
    mock_session.return_value.query.return_value = mock_query

    # Ejecutar la prueba
    response = client.get("/api/v1/profile/nonexistent@example.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "Perfil de usuario no encontrado."}

def test_get_user_profile_success(mocker):
    # Crear un mock para el usuario que se devuelve desde la base de datos
    mock_user = mocker.MagicMock()
    mock_user.email = "test@example.com"
    mock_user.name = "Test User"
    mock_user.created_at = "2023-01-01T00:00:00"
    mock_user.updated_at = "2023-01-02T00:00:00"

    # Crear un mock para la sesión de base de datos
    mock_session = mocker.patch("app.routers.profile.session", autospec=True)

    # Configurar el mock para que `query` devuelva el mock_user
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value.first.return_value = mock_user
    mock_session.return_value.query.return_value = mock_query

    # Realizar la solicitud al endpoint
    response = client.get("/api/v1/profile/test@example.com")

    # Verificar la respuesta
    assert response.status_code == 200
    assert response.json() == {
        "email": "test@example.com",
        "name": "Test User",
        "created_at": "2023-01-01T00:00:00",
        "updated_at": "2023-01-02T00:00:00",
    }

def test_send_message_success():
    response = client.post(
        "/api/v1/llm/prompt",
        json={"user_id": "123", "message": "Hola"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Interacción con el modelo todavía en desarrollo"}

def test_send_message_invalid_request():
    response = client.post(
        "/api/v1/llm/prompt",
        json={"user_id": "123"}
    )
    assert response.status_code == 422  # Error de validación


def test_get_statistics_success():
    response = client.get("/api/v1/stats/summary")
    assert response.status_code == 200
    assert "total_messages" in response.json()
    assert "unique_users" in response.json()


def test_healthcheck_success():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "API funcionando correctamente. Interacciones con el LLM todavía en desarrollo."
    }
