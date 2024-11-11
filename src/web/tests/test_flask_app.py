from app.models import User
from flask import url_for

# Tests para el modelo User
def test_user_creation(app, user):
    with app.app_context():
        assert user.name == "testuser"
        assert user.email == "test@example.com"
        assert user.check_password("mysecretpassword")

def test_user_password_hashing(app, user):
    with app.app_context():
        user.set_password("anotherpassword")
        assert user.check_password("anotherpassword")
        assert not user.check_password("wrongpassword")

# Tests para autenticación
def test_login_required(client):
    # Probar que las rutas protegidas requieran autenticación
    response = client.get(url_for("auth.index"))
    assert response.status_code == 302
    assert "/login" in response.headers["Location"] 

def test_user_login(client):
    # Probar el inicio de sesión
    response = client.post(url_for("auth.login"), data={"email": "test@example.com", "password": "mysecretpassword"}, follow_redirects=True)
    assert response.status_code == 200  # Comprobar solo el redireccionamiento exitoso

def test_invalid_user_login(client):
    # Probar inicio de sesión con credenciales incorrectas, esperando redirección
    response = client.post(url_for("auth.login"), data={"email": "wrong@example.com", "password": "wrongpassword"})
    assert response.status_code == 302

def test_user_registration(client):
    # Probar el registro de un nuevo usuario
    response = client.post(url_for("auth.register"), data={
        "name": "newuser",
        "email": "new@example.com",
        "password": "newpassword",
        "confirm_password": "newpassword"
    }, follow_redirects=True)
    assert response.status_code == 200

    # Verificar que el usuario fue creado
    with client.application.app_context():
        user = User.query.filter_by(email="new@example.com").first()
        assert user is not None
        assert user.name == "newuser"

def test_logout(client, user):
    # Primero, iniciar sesión
    client.post(url_for("auth.login"), data={"email": "test@example.com", "password": "mysecretpassword"})
    
    # Luego, realizar logout
    response = client.get(url_for("auth.logout"), follow_redirects=True)
    assert response.status_code == 200
    assert "/login" in response.request.path

# Tests para la creación de la aplicación
def test_app_creation(app):
    assert app is not None
    assert app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
