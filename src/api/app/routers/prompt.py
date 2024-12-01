from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.logger_config import logger


prompt_router = APIRouter()

class MessageRequest(BaseModel):
    user_id: str
    message: str

class MessageResponse(BaseModel):
    response: str

@prompt_router.post("/prompt", response_model=MessageResponse)
def send_message(request: MessageRequest):
    try:
        logger.info(f"Recibido mensaje del usuario {request.user_id}: {request.message}")
        response_text = "Interacción con el modelo todavía en desarrollo"
        logger.info(f"Respuesta generada para el usuario {request.user_id}: {response_text}")
        return MessageResponse(response=response_text)
    except Exception as e:
        logger.error(f"Error al procesar el mensaje del usuario {request.user_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Error al procesar el mensaje: {e}")