import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

from app.dispatcher import dp
from app.settings import settings


async def main() -> None:
    session = AiohttpSession(api=settings.api)
    bot = Bot(token=settings.token, session=session)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
