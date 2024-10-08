from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.inline_keyboards import settings
from app.states import States

router = Router()


@router.message(States.BASE_WORK, F.text == '/about')
async def handler_command_about(message: Message):
    text_answer = """
Немного о боте!

Это бот для удобной работы с расписанием в НГТУ им. Р. Е. Алексеева.
В этом боте вы можете получить расписание для вашего курса, направления, круппы
с учётом некоторых особенностей (по типу чённости недели). Расписане может быть полученно
как относительно текущего дня или по дням недели (расписание понедельника, вторника, среды ...).

Сам бот был сделан энтузиастами без средств к существованию, так что ваша потдержка проекта очень
важна для нас (самое важное - сервера). Реквезиты для потдержки проекта можете посмотреть по комманде
/help.
    """
    await message.answer(text_answer)


@router.message(States.BASE_WORK, F.text == '/help')
async def handler_command_help(message: Message):
    answer_text = """
Потдержка проекта!
    
Наш проект можно (а ,может быть, и нужно) потдержать средствами.
Для этого можете использовать перевод по номеру (+79030543600).
    """
    await message.answer(answer_text)


@router.message(States.BASE_WORK, F.text == '/settings')
async def handler_command_setting(message: Message):
    answer_text = """
Меню!

Для изменения параметров нажмите на соответствующую кнопку ниже.
    """
    await message.answer(answer_text, reply_markup=settings)
