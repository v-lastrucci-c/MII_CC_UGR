from datetime import datetime, timezone
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

from app.logger_config import logger
from app.internal.models import Responses
from app.internal.async_openai import AsyncOpenAi
from app.internal.db import session

prompt_router = APIRouter()
class MessageRequest(BaseModel):
    user_id: str
    message: str = Field(..., min_length=1, description="El mensaje del usuario no puede estar vacío")

class MessageResponse(BaseModel):
    message: str

@prompt_router.post("/prompt", response_model=MessageResponse)
async def send_message(request: MessageRequest):
    """
    Procesa un mensaje enviado por el usuario, genera una respuesta simulada y la almacena en la base de datos.
    """
    db = session()
    try:
        # Log del mensaje recibido
        logger.info(f"Recibido mensaje del usuario {request.user_id}: {request.message}")
        llm_model = AsyncOpenAi()
        response_text = await llm_model.llm_response(user_question=request.message)
        
        logger.info("Guardando respuesta en la base de datos...")
        new_response = Responses(response=response_text, created_at=datetime.now(timezone.utc))
        db.add(new_response)
        db.commit()

        logger.info(f"Respuesta generada para el usuario {request.user_id}: {response_text}")

        return MessageResponse(message=response_text)

    except Exception as e:
        logger.error(f"Error al procesar el mensaje del usuario {request.user_id}: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")
    finally:
        db.close()
