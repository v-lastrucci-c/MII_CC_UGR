from fastapi import APIRouter
from app.logger_config import logger

stats_router = APIRouter()

stats_data = {
    "total_messages": 0,
    "unique_users": set()
}

@stats_router.get("/summary", response_model=dict)
def get_statistics():
    try:
        logger.info("Recuperando estadísticas de uso")
        return {
            "total_messages": stats_data["total_messages"],
            "unique_users": len(stats_data["unique_users"])
        }
    except Exception as e:
        logger.error(f"Error al recuperar estadísticas: {e}")
        raise e