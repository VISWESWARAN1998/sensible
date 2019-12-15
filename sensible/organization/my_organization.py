# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection


class MyOrganization(Resource):

    def get(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id from organization where user_id=%s", (user_id, ))
            result = cursor.fetchall()
            return jsonify(
                {
                    "organization_list": result
                }
            )
        finally:
            cursor.close()
            connection.close()