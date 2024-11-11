"""
Contiene los modelos relacionados con
 la base de datos.

Uso:
    ./models.py
"""
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from datetime import datetime, timezone


class User(db.Model):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(50), primary_key=True)
    password_hash: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def set_password(self, value: str) -> None:
        """Guardar la contraseña como un hash por seguridad."""
        self.password_hash = generate_password_hash(value)

    # allow password = "..." to set a password
    password = property(fset=set_password)

    def check_password(self, value: str) -> bool:
        return check_password_hash(self.password_hash, value)

    def __repr__(self):
        return f'<User {self.email}>'