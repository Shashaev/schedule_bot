from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text == '/start')
async def handler_command_start(message: Message):
    text_answer = """
Привет новый пользователь!\n
Это бот с расписание для студетнов НГТУ им. Р. Е. Алексеева.
Что бы начать пользоваться ботом нужно настроить ваш профиль.
    """
    await message.answer(text_answer)

