from sql.conection import connection


def execute_sql(path_file: str, param: dict):
    try:
        with connection.cursor() as cus:
            with open(path_file, encoding='utf-8') as f:
                sql_query = f.read()
            cus.execute(sql_query, param)
        connection.commit()
    except BaseException as e:
        print('Exception in execute_sql:')
        print(e)
