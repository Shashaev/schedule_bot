import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeDefault
from app.config import TOKEN
from app.handlers import specials_handlers
from app.handlers import menu_handlers
from app.keyboards.specials_keyboards import menu


async def run_bot():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(specials_handlers.router)
    dp.include_router(menu_handlers.router)

    await bot.set_my_commands(menu, scope=BotCommandScopeDefault())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run_bot())
