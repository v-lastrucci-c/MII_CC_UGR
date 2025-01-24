"""
Contiene los modelos relacionados con
 la base de datos.

Uso:
    ./models.py
"""
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    # Columnas de la tabla
    email = Column(String(50), primary_key=True, nullable=False)  # Clave primaria
    name = Column(String(25), nullable=False)  # Nombre del usuario
    password_hash = Column(String, nullable=False)  # Hash de la contraseña
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Fecha de creación
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Fecha de actualización

    def __repr__(self):
        return f"<User email={self.email} name={self.name}>"

class Responses(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    response = Column(String(50))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
