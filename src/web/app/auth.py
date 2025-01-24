"""
Contiene las funciones relacionadas con
 el inicio de sesión de usuarios.

Uso:
    ./auth.py
"""
import os
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.logger_config import logger
from app.models import User
from app import db

from dotenv import load_dotenv
load_dotenv(override=True)

bp = Blueprint("auth", __name__)

def login_required(view):
    """Redirect anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        logger.debug("Verificando si el usuario está autenticado antes de acceder a la vista protegida.")
        if g.get("user") is None:
            logger.warning("Intento de acceso no autenticado. Redirigiendo a la página de inicio de sesión.")
            flash("Debe iniciar sesión para acceder a la página principal.", category="error")
            return redirect(url_for("auth.login"))
        logger.debug("Usuario autenticado. Permitiendo el acceso a la vista protegida.")
        return view(**kwargs)
    return wrapped_view

@bp.route('/')
@login_required
def index():
    logger.info("Cargando página principal para usuario autenticado.")
    return render_template('index.html', apiBaseUrl=os.getenv("API_BASE_URL"), email=g.user.email)

@bp.before_app_request
def load_logged_in_user():
    """
    Si la identificación de usuario está almacenada en la sesión,
    cargamos el objeto de usuario desde la base de datos en ``g.user``.
    """
    logger.debug("Intentando cargar el usuario autenticado desde la sesión.")
    user_email = session.get("user_email")

    if user_email is not None:
        logger.info(f"Usuario encontrado en la sesión: {user_email}. Intentando cargar desde la base de datos.")
        g.user = db.session.get(User, user_email)
        if g.user:
            logger.info(f"Usuario cargado exitosamente: {user_email}")
        else:
            logger.warning("No se pudo cargar el usuario desde la base de datos.")
    else:
        logger.debug("No hay usuario autenticado en la sesión.")
        g.user = None

@bp.route("/register", methods=("GET", "POST"))
def register():
    """Registrar un nuevo usuario

    Valida que el nombre de usuario no esté ya en uso. Hashea la
    contraseña por seguridad.
    """
    if request.method == "POST":
        logger.info("Procesando formulario de registro.")
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        error = None

        if not name or not email or not password:
            error = "Rellene todos los campos."
            logger.error("Campos incompletos en el formulario de registro.")
        elif db.session.query(User).filter_by(email=email).first() is not None:
            error = f"El usuario: {name} ya está registrado."
            logger.warning(f"Intento de registro con un correo ya registrado: {email}.")

        if error is None:
            logger.info(f"Registrando nuevo usuario: {name}, {email}.")
            db.session.add(User(name=name, email=email, password=password))
            db.session.commit()
            logger.info("Usuario registrado exitosamente.")
            flash("Registro exitoso. Ahora puedes iniciar sesión.",
                  category="success")
            return redirect(url_for("auth.login"))

        logger.warning(f"Error durante el registro: {error}")
        flash(error, category="error")
        return redirect(url_for("auth.register"))

    logger.debug("Cargando formulario de registro.")
    return render_template("auth/register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    """Iniciar sesión agregando el email del usuario a la sesión."""
    if request.method == "POST":
        logger.info("Procesando formulario de inicio de sesión.")
        email = request.form["email"]
        password = request.form["password"]

        try:
            error = None
            select = db.select(User).filter_by(email=email)
            user = db.session.execute(select).scalar()
        except Exception as error:
            logger.error(f"Fallo en la conexión con la base de datos: {error}")
            flash("Fallo en la conexión con la base de datos.", category="error")
            return redirect(url_for("auth.login"))

        if user is None:
            error = "Usuario incorrecto."
            logger.warning(f"Intento de inicio de sesión con email no registrado: {email}.")
        elif not user.check_password(password):
            error = "Contraseña incorrecta."
            logger.warning(f"Intento de inicio de sesión con contraseña incorrecta: {email}.")

        if error is None:
            logger.info(f"Inicio de sesión exitoso para el usuario: {email}.")
            session.clear()
            session["user_email"] = user.email
            flash("Inicio de sesión exitoso.", category="success")
            return redirect(url_for("auth.index"))

        logger.error(f"Error durante el inicio de sesión: {error}")
        flash(error, category="error")
        return redirect(url_for("auth.login"))

    logger.debug("Cargando formulario de inicio de sesión.")
    return render_template("auth/login.html")

@bp.route("/logout")
def logout():
    """Borrar la sesión actual."""
    logger.info("Cerrando sesión para el usuario actual.")
    session.clear()
    flash("Ha cerrado sesión exitosamente.", category="success")
    logger.info("Sesión cerrada y redirigiendo a la página de inicio de sesión.")
    return redirect(url_for("auth.login"))