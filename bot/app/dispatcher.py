from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from app.settings import settings

CONFETTI_EFFECT_ID = "4972316941755613185"
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Open Web App", url=str(settings.web_app_url))]
        ]
    )
    full_name = "my friend"
    if message.from_user is not None:
        full_name = message.from_user.full_name
    await message.answer(
        f"Hello, {full_name}!\nThis bot will allow you and your friends to keep track of how much time is left until your birthday!",
        reply_markup=markup,
        message_effect_id=CONFETTI_EFFECT_ID,
    )
