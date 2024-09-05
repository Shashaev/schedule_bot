from sql.utils import execute_sql
from datetime import timedelta


def get_schedule(user_name: str, week_day: str) -> str:
    """
    Возвращает расписание пользователя для определённого дня недели
    :param user_name: username пользователя
    :param week_day: день недели
    :return: строку, илюстрирующую расписание или его отсутствие
    """
    text_answer = 'По вашим заданным параметрам ничего не нашлось'
    data = execute_sql('sql/command_sql/select/select_data_user.sql',
                       {'user_name': user_name, 'day_week': week_day})
    if not data:
        return text_answer
    formated_schedule = ''
    for el in data:
        formated_schedule += __get_formated_schedule(el.get('name'), el.get('start_time'), el.get('end_time'),
                                                     el.get('displayed'), el.get('features'), el.get('office'))
        formated_schedule += '#' * 25
    return formated_schedule


def __get_formated_schedule(name: str, start_time: timedelta, end_time: timedelta,
                            displayed_lecturer: str = None, features: str = None, office: int = None):
    formated_schedule = f"""
Предмет: {name}
Время: {str(start_time)[:-3]} - {str(end_time)[:-3]}
"""
    if office:
        formated_schedule += f'Кабинет: {office}\n'
    if displayed_lecturer:
        formated_schedule += f'Преподаватель: {displayed_lecturer}\n'
    if features:
        formated_schedule += f'Особенности: {features}\n'
    return formated_schedule


if __name__ == '__main__':
    import os

    os.chdir(os.getcwd().replace(r'\app', ''))
    print(get_schedule('ShashaevKirill', 'monday'))
