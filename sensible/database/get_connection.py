# SWAMI KARUPPASWAMI THUNNAI

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import platform


def get_connection():
    if "linux" in platform:
        connection = pymysql.connect(
            host="127.0.0.1", user="root", password="#xoW4TOJnKz7",
            db="sensible", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor
        )
    else:
        connection = pymysql.connect(
            host="127.0.0.1", user="root", password="visweswaran",
            db="sensible", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor
        )
    return connection


def orm_connection():
    if "linux" in platform:
        engine = create_engine("mysql+pymysql://root:#xoW4TOJnKz7@127.0.0.1/medease")
    else:
        engine = create_engine("mysql+pymysql://root:visweswaran@127.0.0.1/medease")
    return engine


Base = declarative_base()

