# SWAMI KARUPPASWAMI THUNNAI

from flask import jsonify


class SensibleException:

    INVALID_PHONE = 1
    PHONE_EXISTS = 2
    INVALID_CURRENCY_CODE = 3
    DATA_NOT_PRESENT = 4
    INCORRECT_PASSWORD = 5

    EXCEPTION_DICT = {
        INVALID_PHONE: "The phone number which you have entered is invalid.",
        PHONE_EXISTS: "The phone number exists on our system",
        INVALID_CURRENCY_CODE: "The currency code is invalid",
        DATA_NOT_PRESENT: "The requested data is not present in the database.",
        INCORRECT_PASSWORD: "The password is incorrect!"
    }

    @staticmethod
    def raise_exception(exception_id):
        response = jsonify(
            {
                "exception_id": exception_id,
                "message": SensibleException.EXCEPTION_DICT[exception_id]
            }
        )
        response.status_code = 400
        return response