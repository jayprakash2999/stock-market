from mysql.connector import connect
from database.config import DB_CONFIG


def get_database():
    connection = None
    try:
        connection = connect(**DB_CONFIG)
        yield connection
    finally:
        if connection is not None:
            connection.close()
