from aiogram.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton


menu = [BotCommand(command='/about', description='Описание бота'),
        BotCommand(command='/help', description='Помощь проекту'),
        BotCommand(command='/settings', description='Настройки пользователя')]

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Вчера'), KeyboardButton(text='Сегодня'), KeyboardButton(text='Завтра')],
        [KeyboardButton(text='Дни недели')]
])
