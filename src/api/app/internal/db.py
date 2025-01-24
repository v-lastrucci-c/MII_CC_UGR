import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.logger_config import logger

logger.info("Configurando conexion a la base de datos...")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")
engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
