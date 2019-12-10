# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from user.helper import sensible_token


class MyTag(Resource):

    @sensible_token
    def get(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id, name, hexcolour from tag where user_id=%s", (user_id, ))
            result = cursor.fetchall()
            return jsonify(
                {
                    "tag_list": result
                }
            )
        finally:
            cursor.close()
            connection.close()
