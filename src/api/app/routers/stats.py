from fastapi import APIRouter
from app.logger_config import logger

from app.internal.models import Responses
from app.internal.models import User
from app.internal.db import session

stats_router = APIRouter()

# Obtener estadísticas de la base de datos
def update_stats_data():
    db = session()
    try:
        logger.info("Actualizando estadísticas desde la base de datos...")
        total_messages = db.query(Responses).count()
        users = db.query(User).count()

        return {
            "total_messages": total_messages,
            "users": users
        }
    except Exception as e:
        logger.error(f"Error al actualizar estadísticas: {e}")
        raise e
    finally:
        db.close()

@stats_router.get("/summary", response_model=dict)
def get_statistics():
    try:
        logger.info("Recuperando estadísticas de uso...")
        stats_data = update_stats_data()
        return {
            "total_messages": stats_data["total_messages"],
            "users": stats_data["users"]
        }
    except Exception as e:
        logger.error(f"Error al recuperar estadísticas: {e}")
        raise e
