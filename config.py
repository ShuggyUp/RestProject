from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):
    """Настройки базы данных"""

    db_host: str = Field('localhost', env='DB_HOST')
    db_port: str = Field('5432', env='DB_PORT')
    db_name: str = Field('postgres', env='DB_NAME')
    db_user: str = Field('postgres', env='DB_USER')
    db_pass: str = Field(..., env='DB_PASS')

    class Config:
        env_file = '.env'


class UvicornSettings(BaseSettings):
    """Настройки сервера"""

    host: str = Field('127.0.0.1', env='SERVER_HOST')
    port: int = Field(8000, env='SERVER_PORT')

    class Config:
        env_file = '.env'


db_settings = DatabaseSettings()
server_settings = UvicornSettings()
