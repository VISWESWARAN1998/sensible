# SWAMI KARUPPASWAMI THUNNAI

import pymysql


def get_connection():
    connection = pymysql.connect(
        host="127.0.0.1", user="root", password="visweswaran",
        db="sensible", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor
    )
    return connection
