# SWAMI KARUPPASWAMI THUNNAI


def validate_phone_number(phone_number):
    phone_number = str(phone_number)
    if len(phone_number) != 10:
        return False
    try:
        int(phone_number)
        # Phone number should not be negative
        if int(phone_number) < 0:
            return False
        return True
    except ValueError:
        return False
