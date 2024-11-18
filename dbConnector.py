import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # e.g., 'localhost'
        user='root',
        password='ManasPhanse22',
        database='school'
    )
    try:
        yield connection
    finally:
        connection.close()
