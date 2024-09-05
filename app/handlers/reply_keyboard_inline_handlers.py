from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.utils import get_schedule

router = Router()


@router.callback_query(F.data.startswith('week_days_'))
async def handler_callback_query_week_days(callback: CallbackQuery):
    week_day = callback.data.split('_')[-1]
    text_answer = get_schedule(callback.from_user.username, week_day)
    await callback.message.answer(text_answer)
