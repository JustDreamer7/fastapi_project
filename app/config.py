import os
from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import AnyUrl, PostgresDsn, RedisDsn, validator # Классы для построения url в БД
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_PORT: int
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}'
            f':{self.DB_PORT}/{self.DB_NAME}')

    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
