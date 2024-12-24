import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost <or any other server>',
        user='root',
        password='<your password>',
        database='school'
    )
    try:
        yield connection
    finally:
        connection.close()
