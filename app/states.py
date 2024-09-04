from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    BASE_WORK = State()
    WRITE_GROUP = State()
