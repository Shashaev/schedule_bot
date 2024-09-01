import pymysql
from app.config import USER, PASSWORD, HOST, DATABASE, PORT


connection = pymysql.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    cursorclass=pymysql.cursors.DictCursor
)

print('####################')
