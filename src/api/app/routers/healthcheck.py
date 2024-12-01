from fastapi import APIRouter
from app.logger_config import logger

healthcheck_router = APIRouter()

@healthcheck_router.get("/health", response_model=dict)
def healthcheck():
    try:
        logger.info("Comprobación de estado de la API")
        return {
            "status": "ok",
            "message": "API funcionando correctamente. Interacciones con el LLM todavía en desarrollo."
            }
    except Exception as e:
        logger.error(f"Error en el healthcheck: {e}")
        raise e