from sql.utils import execute_sql


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
    data = data[0]
    formated_schedule = __get_formated_schedule(data.get('name'), data.get('start_time'), data.get('end_time'),
                                                data.get('displayed'), data.get('features'))
    return formated_schedule


def __get_formated_schedule(name: str, start_time, end_time,
                            displayed_lecturer: str = None, features: str = None):
    formated_schedule = f"""
Предмет: {name}
Время проведения: {start_time} - {end_time}
"""
    if displayed_lecturer:
        formated_schedule += f'Преподаватель: {displayed_lecturer}\n'
    if features:
        formated_schedule += f'Особенности: {features}'
    return formated_schedule
