from os import getenv

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Базовый класс настроек."""
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = getenv('POSTGRES_HOST', 'postgres')
    POSTGRES_PORT: str = getenv('POSTGRES_PORT', '5432')

    ELASTICSEARCH_HOST: str = 'elasticsearch'
    ELASTICSEARCH_PORT: str = getenv('ELASTICSEARCH_PORT')
    DISCOVERY_TYPE: str = getenv('DISCOVERY_TYPE')
    SECURITY_MODE: str = getenv('SECURITY_MODE')
    ES_JAVA_OPTS: str = getenv('ES_JAVA_OPTS')
    ELASTIC_PASSWORD: str = getenv('ELASTIC_PASSWORD')
    CLUSTER_NAME: str = getenv('CLUSTER_NAME')

    class Config:
        env_file = getenv('ENV', '.env')
        extra = "ignore"


settings = Settings()
