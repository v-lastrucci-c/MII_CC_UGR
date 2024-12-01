from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, HTTPException

from app.logger_config import logger
from app.internal.models import User

import os
from dotenv import load_dotenv
load_dotenv(override=True)

profile_router = APIRouter()

logger.info("Configurando conexion a la base de datos...")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")
engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class UserProfile(BaseModel):
    email: str
    name: str
    created_at: datetime
    updated_at: datetime

@profile_router.get("/{user_email}", response_model=UserProfile)
def get_user_profile(user_email: str):
    """
    Obtiene el perfil de usuario desde la base de datos utilizando SQLAlchemy.
    """
    db = session()
    try:
        # Buscar usuario en la base de datos
        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            logger.warning(f"Perfil no encontrado para el usuario {user_email}")
            raise HTTPException(status_code=404, detail="Perfil de usuario no encontrado.")

        logger.info(f"Perfil recuperado para el usuario {user_email}")
        return UserProfile(
            email=user.email,
            name=user.name,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
    except HTTPException as http_exc:
        # Si es una excepción HTTP, simplemente vuelve a lanzarla
        raise http_exc
    except Exception as e:
        # Manejar otros errores como errores internos del servidor
        logger.error(f"Error al recuperar el perfil del usuario {user_email}: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")
    finally:
        db.close()