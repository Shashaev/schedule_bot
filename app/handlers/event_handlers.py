from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states import States
from sql.utils import execute_sql

router = Router()


@router.message(States.WRITE_GROUP)
async def handler_state_write_group(message: Message, state: FSMContext):
    text_answer = f"""
Вы изменили настройки вашего профиля.
Теперь ваша группа: {message.text.upper()}.
    """
    execute_sql('sql/command_sql/update/update_user_group.sql',
                {'group': message.text.upper(),
                 'user_name': message.from_user.username})
    await state.set_state(States.BASE_WORK)
    await message.answer(text_answer)
