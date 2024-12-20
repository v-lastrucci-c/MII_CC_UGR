"""
Contiene la fabricación de la aplicación Flask.

Uso:
    ./__init__.py
"""
import os
import click

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from app.logger_config import logger


load_dotenv(override=True)

db = SQLAlchemy()


def create_app():
    logger.info("Initializing the Flask app...")
    app = Flask(__name__, instance_relative_config=True,
                static_folder="../static", template_folder="../templates")
    
    logger.info("Configuring the Flask app...")
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "ai-aichronos-secret-key"),
        SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI"),
        DEBUG=True,
        PORT=5000
    )    

    logger.info("Adding extra configurations...")
    if os.getenv("TEST_CONFIG") is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(os.getenv("TEST_CONFIG"))

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    logger.info("Initializing the database...")
    db.init_app(app)
    app.cli.add_command(init_db_command)

    logger.info("Registering blueprints...")
    from . import auth
    app.register_blueprint(auth.bp, url_prefix="/")

    return app


def init_db():
    logger.info("Dropping all tables...")
    db.drop_all()
    logger.info("Creating all tables...")
    db.create_all()
    logger.info("Database initialized successfully.")

@click.command("init-db")
def init_db_command():
    """Borrar los datos existentes y crear nuevas tablas."""
    init_db()
    click.echo("Base de datos Inicializada.")
