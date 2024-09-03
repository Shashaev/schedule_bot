from aiogram import Router, F
from aiogram.types import Message
from sql.conection import connection


router = Router()


@router.message(F.text == '/start')
async def handler_command_start(message: Message):
    text_answer = """
Привет, новый пользователь!\n
Это бот с расписанием для студетнов НГТУ им. Р. Е. Алексеева.
Чтобы начать пользоваться ботом нужно настроить ваш профиль.
    """
    try:
        with connection.cursor() as cus:
            with open('sql/comonds_sql/insert/include_user.sql') as f:
                sql_query = f.readline()
            cus.execute(sql_query, {'name': message.from_user.username})
        connection.commit()
    except BaseException as e:
        print(e)
    await message.answer(text_answer)
