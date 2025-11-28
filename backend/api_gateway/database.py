# api_gateway/databases.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values, load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
# Charge le .env

load_dotenv(dotenv_path)

config_data = dotenv_values(dotenv_path)

ENV = config_data.get('ENV')
USE_SQLITE = config_data.get('USE_SQLITE', '').lower() == 'true'

if USE_SQLITE:
    # Utiliser SQLite pour les tests
    DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
elif ENV == 'Prod':
    DATABASE_URL = f"postgresql+psycopg2://{config_data.get('DB_USER_PROD')}:{config_data.get('DB_PASSWORD_PROD')}@{config_data.get('DB_HOST_PROD')}:{config_data.get('DB_PORT_PROD')}/{config_data.get('DB_NAME_PROD')}"
    engine = create_engine(DATABASE_URL)
else:
    DATABASE_URL = f"postgresql+psycopg2://{config_data.get('DB_USER')}:{config_data.get('DB_PASSWORD')}@{config_data.get('DB_HOST')}:{config_data.get('DB_PORT')}/{config_data.get('DB_NAME')}"
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
