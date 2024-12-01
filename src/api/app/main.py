from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

from app.logger_config import logger

from app.routers.healthcheck import healthcheck_router
from app.routers.stats import stats_router
from app.routers.prompt import prompt_router
from app.routers.profile import profile_router


logger.info("Iniciando: API AICHRONOS...")
app = FastAPI(
    title="API AICHRONOS",
    description="",
    version="1.0.0"
)

logger.info("Configurando CORS...")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],  # Especifica orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)


logger.info("Registrando routers...")
app.include_router(prompt_router, prefix="/api/v1/llm", tags=["Prompts"])
app.include_router(profile_router, prefix="/api/v1/profile", tags=["User Profiles"])
app.include_router(stats_router, prefix="/api/v1/stats", tags=["Statistics"])
app.include_router(healthcheck_router, prefix="/api/v1", tags=["Healthcheck"])
