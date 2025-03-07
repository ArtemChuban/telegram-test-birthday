from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str


class BotSettings(BaseModel):
    token: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_nested_delimiter="__"
    )
    bot: BotSettings
    database: DatabaseSettings


settings = Settings()

TORTOISE_ORM_SETTINGS = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": settings.database.host,
                "port": settings.database.port,
                "user": settings.database.user,
                "password": settings.database.password,
                "database": settings.database.database,
            },
        },
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
        }
    },
}
