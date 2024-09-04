from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Группа', callback_data='change_group')],
    [InlineKeyboardButton(text='Подгруппа', callback_data='change_local_group')],
    [InlineKeyboardButton(text='Подгруппа по английскому', callback_data='change_local_group_english')],
    [InlineKeyboardButton(text='Чётность недели', callback_data='change_parity_week')]
])

local_groups = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Первая подгруппа', callback_data='change_local_group_1')],
    [InlineKeyboardButton(text='Вторая подгруппа', callback_data='change_local_group_2')]
])

local_groups_english = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Первая подгруппа', callback_data='change_local_group_english_1')],
    [InlineKeyboardButton(text='Вторая подгруппа', callback_data='change_local_group_english_2')]
])

parity_week = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Чётная', callback_data='change_parity_week_even')],
    [InlineKeyboardButton(text='Нечётная', callback_data='change_parity_week_odd')]
])
