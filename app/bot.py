import asyncio
from aiogram import Bot, Dispatcher
from app.config import TOKEN


async def run_bot():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_routers()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run_bot())
