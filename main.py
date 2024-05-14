import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.utils.i18n import FSMI18nMiddleware, I18n

from admin.admin import admin_router
from config import TOKEN
from routers.handler import handler_router
from routers.send_to_admin import send_router
from routers.user import user_router

dp = Dispatcher()


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    command_list = [
        BotCommand(command='start', description='Botni boshlash'),
        BotCommand(command='help', description='Yordam kerakmi'),
    ]
    await bot.set_my_commands(command_list)


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    await bot.delete_my_commands()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    i18n = I18n(path='locales', default_locale='uz')
    dp.update.outer_middleware.register(FSMI18nMiddleware(i18n))
    dp.include_routers(
        handler_router,
        user_router,
        admin_router,
        send_router
    )
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
