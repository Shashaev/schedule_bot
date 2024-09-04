from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sql.utils import execute_sql
from app.states import States

router = Router()


@router.message(F.text == '/start')
async def handler_command_start(message: Message, state: FSMContext):
    text_answer = """
Привет, новый пользователь!\n
Это бот с расписанием для студетнов НГТУ им. Р. Е. Алексеева.
Чтобы начать пользоваться ботом нужно настроить ваш профиль.
    """
    execute_sql('sql/command_sql/insert/include_user.sql',
                {'name': message.from_user.username})
    await state.set_state(States.BASE_WORK)
    await message.answer(text_answer)
