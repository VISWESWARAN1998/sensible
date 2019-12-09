# SWAMI KARUPPASWAMI THUNNAI

# Author Name: Visweswaran N
# Email: visweswaran.nagasivam98@gmail.com
# Copyright (C): Visweswaran N
# Date: 09-02-2019


def is_float(value):
    """
    This function will check whether the supplied value is float or not

    :param value: The value to be checked for float

    :return: True if it is an float else it will return false
    """
    try:
        float(value)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
