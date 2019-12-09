# SWAMI KARUPPASWAMI THUNNAI

from validator.integer import is_int
from database.get_connection import get_connection


def is_valid_currency(currency):
    if not is_int(currency):
        return False
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select name from currency where id=%s limit 1", (currency, ))
        result = cursor.fetchone()
        if result:
            return True
        return False
    finally:
        cursor.close()
        connection.close()
