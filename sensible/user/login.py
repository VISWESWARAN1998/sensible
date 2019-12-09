# SWAMI KARUPPASWAMI THUNNAI

from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from sensible_exception import SensibleException
from user.helper import verify_password, generate_token


class UserLogin(Resource):

    def post(self):
        phone = request.json["phone"]
        password = request.json["password"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id, password_hash from user_credential where phone=%s limit 1", (phone, ))
            result = cursor.fetchone()
            if result is None:
                return SensibleException.raise_exception(SensibleException.DATA_NOT_PRESENT)
            if not verify_password(password, result["password_hash"]):
                return SensibleException.raise_exception(SensibleException.INCORRECT_PASSWORD)
            _token = generate_token(result["id"], result["password_hash"])
            return jsonify(
                {
                    "message": _token
                }
            )
        finally:
            cursor.close()
            connection.close()