from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from app.states import States
from app.keyboards.inline_keyboards import local_groups, local_groups_english, parity_week
from sql.utils import execute_sql

router = Router()


@router.callback_query(F.data == 'change_group')
async def handler_callback_query_change_group(callback: CallbackQuery, state: FSMContext):
    text_answer = """
Для изменения напишите вашу группу.
Пример 23-ИВТ-5 (регистр не учитываеться)
    """
    await callback.message.answer(text_answer)
    await state.set_state(States.WRITE_GROUP)


@router.callback_query(F.data == 'change_local_group')
async def handler_callback_query_change_group(callback: CallbackQuery):
    text_answer = """
Для изменения выберите вашу подгруппу
    """
    await callback.message.answer(text_answer, reply_markup=local_groups)


@router.callback_query(F.data == 'change_local_group_english')
async def handler_callback_query_change_group(callback: CallbackQuery):
    text_answer = """
Для изменения выберите вашу подгруппу по английскому
    """
    await callback.message.answer(text_answer, reply_markup=local_groups_english)


@router.callback_query(F.data.startswith('change_local_group_english_'))
async def handler_callback_query_change_group(callback: CallbackQuery):
    text_answer = f"""
Вы изменили настройки вашего профиля.
Теперь ваша подгруппа по английскому: {callback.data.split('_')[-1]}.
    """
    execute_sql('sql/command_sql/update/update_user_local_group_english.sql', {
        'local_group_english': int(callback.data.split('_')[-1]),
        'user_name': callback.from_user.username
    })
    await callback.message.answer(text_answer)


@router.callback_query(F.data.startswith('change_local_group_'))
async def handler_callback_query_change_group(callback: CallbackQuery):
    text_answer = f"""
Вы изменили настройки вашего профиля.
Теперь ваша подгруппа: {callback.data.split('_')[-1]}.
    """
    execute_sql('sql/command_sql/update/update_user_local_group.sql', {
        'local_group': int(callback.data.split('_')[-1]),
        'user_name': callback.from_user.username
    })
    await callback.message.answer(text_answer)


@router.callback_query(F.data == 'change_parity_week')
async def handler_callback_query_change_group(callback: CallbackQuery):
    text_answer = """
Для изменения выберите чётность недели
    """
    await callback.message.answer(text_answer, reply_markup=parity_week)


@router.callback_query(F.data.startswith('change_parity_week_'))
async def handler_callback_query_change_group(callback: CallbackQuery):
    text_answer = f"""
Вы изменили настройки вашего профиля.
Теперь чётность недели: {['нечётная', 'чётная'][callback.data.split('_')[-1] == 'even']}.
    """
    execute_sql('sql/command_sql/update/update_user_parity_week.sql', {
        'parity_week': callback.data.split('_')[-1],
        'user_name': callback.from_user.username
    })
    await callback.message.answer(text_answer)
