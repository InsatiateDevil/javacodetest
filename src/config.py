import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Загрузка переменных окружения из .env
    load_dotenv()

    # Блок базы данных
    db_name: str = os.getenv('POSTGRES_DB')
    db_user: str = os.getenv('POSTGRES_USER')
    db_pass: str = os.getenv('POSTGRES_PASSWORD')
    db_host: str = os.getenv('POSTGRES_HOST')
    db_port: int = os.getenv('POSTGRES_PORT')
    db_url: str = f'postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    db_echo: bool = os.getenv('DB_ECHO', False) == 'True'


settings = Settings()
