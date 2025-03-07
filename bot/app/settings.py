from aiogram.client.telegram import PRODUCTION, TEST, TelegramAPIServer
from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str = Field(alias="TELEGRAM_TOKEN")
    use_test_server: bool = Field(alias="TEST", default=False)
    web_app_url: HttpUrl

    @property
    def api(self) -> TelegramAPIServer:
        if self.use_test_server:
            return TEST
        return PRODUCTION


settings = Settings()
