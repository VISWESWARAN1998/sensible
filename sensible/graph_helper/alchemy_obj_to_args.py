# SWAMI KARUPPASWAMI THUNNAI

from sqlalchemy import inspect


def obj_to_args(alchemy_object):
    result = dict()
    for columns in inspect(alchemy_object).mapper.column_attrs:
        key = columns.key
        value = getattr(alchemy_object, key)
        result[key] = value
    return result