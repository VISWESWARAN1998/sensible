# SWAMI KARUPPASWAMI THUNNAI

# Author Name: Visweswaran N
# Email: visweswaran.nagasivam98@gmail.com
# Copyright (C): Visweswaran N
# Date: 09-02-2019


def is_int(value):
    """
    This function will check whether the supplied value is integer or not

    :param value: The value to be checked

    :return: True if it is an integer else it will return false
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
