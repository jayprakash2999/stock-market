from mysql.connector import connect
from config import DB_CONFIG


def get_database():
    try:
        connection = connect(**DB_CONFIG)
        yield connection
    finally:
        connection.close()
