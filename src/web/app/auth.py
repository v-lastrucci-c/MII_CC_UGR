"""
Contiene las funciones relacionadas con
 el inicio de sesión de usuarios.

Uso:
    ./auth.py
"""
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.models import User
from app import db

bp = Blueprint("auth", __name__)


def login_required(view):
    """Redirect anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.get("user") is None:
            flash("Debe iniciar sesión para acceder a esta página.", category="error")
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view


@bp.route('/')
@login_required
def index():
    return render_template('index.html')


@bp.before_app_request
def load_logged_in_user():
    """
    Si la identificación de usuario está almacenada en la sesión,
    cargamos el objeto de usuario desde la base de datos en ``g.user``.
    """
    user_email = session.get("user_email")

    if user_email is not None:
        g.user = db.session.get(User, user_email)
    else:
        g.user = None


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Registrar un nuevo usuario

    Valida que el nombre de usuario no esté ya en uso. Hashea la
    contraseña por seguridad.
    """
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        error = None

        if not name or not email or not password:
            error = "Rellene todos los campos."
        elif db.session.query(User).filter_by(email=email).first() is not None:
            error = f"El usuario: {name} ya está registrado."

        if error is None:
            # The name is available, create the user and go to the login page
            db.session.add(User(name=name, email=email, password=password))
            db.session.commit()
            flash("Registro exitoso. Ahora puedes iniciar sesión.",
                  category="success")
            return redirect(url_for("auth.login"))

        flash(error, category="error")
        return redirect(url_for("auth.register"))

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Iniciar sesión agregando el email del usuario a la sesión."""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        error = None
        select = db.select(User).filter_by(email=email)
        user = db.session.execute(select).scalar()

        if user is None:
            error = "Usuario incorrecto."
        elif not user.check_password(password):
            error = "Contraseña incorrecta."

        if error is None:
            # Almacenar la identificación del usuario en una nueva sesión
            session.clear()
            session["user_email"] = user.email
            flash("Inicio de sesión exitoso.", category="success")
            return redirect(url_for("auth.index"))

        flash(error, category="error")
        return redirect(url_for("auth.login"))

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Borrar la sesión actual."""
    session.clear()
    flash("Ha cerrado sesión exitosamente.", category="success")
    return redirect(url_for("auth.login"))
