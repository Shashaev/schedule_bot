import datetime
from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.inline_keyboards import week_days
from app.utils import get_schedule

router = Router()


@router.message(F.text == 'Дни недели')
async def handler_message_week_days(message: Message):
    text_answer = """
Для получения расписания ваберите соответствующий день недели
    """
    await message.answer(text_answer, reply_markup=week_days)


@router.message(F.text == 'Вчера')
@router.message(F.text == 'Сегодня')
@router.message(F.text == 'Завтра')
async def handler_message_get_schedule(message: Message):
    time = datetime.datetime.today().weekday() + (message.text == 'Завтра') - (message.text == 'Вчера')
    time %= 7
    week_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'][time]
    text_answer = get_schedule(message.from_user.username, week_day)
    await message.answer(text_answer)
