# SWAMI KARUPPASWAMI THUNNAI

from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from validator.phone import validate_phone_number
from sensible_exception import SensibleException
from user.helper import hash_password
from validator.currency import is_valid_currency


class UserSignup(Resource):

    def post(self):
        phone = request.json["phone"]
        password = request.json["password"]
        name = request.json["name"]
        profile_picture = request.json["profile_picture"]
        currency_code = request.json["currency"]
        if not validate_phone_number(phone_number=phone):
            return SensibleException.raise_exception(SensibleException.INVALID_PHONE)
        if not is_valid_currency(currency=currency_code):
            return SensibleException.raise_exception(SensibleException.INVALID_CURRENCY_CODE)
        password = hash_password(password)
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id from user_credential where phone=%s limit 1", (phone, ))
            result = cursor.fetchone()
            if result:
                return SensibleException.raise_exception(SensibleException.PHONE_EXISTS)
            cursor.execute("insert into user_credential value(null, null, %s, %s, %s, %s, %s, 0)", (
                phone, password, name, currency_code, profile_picture
            ))
            user_id = cursor.lastrowid
            connection.commit()
            return jsonify(
                {
                    "message": "Account has been created!",
                    "user_id": user_id
                }
            )
        finally:
            cursor.close()
            connection.close()
