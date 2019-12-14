# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from user.helper import sensible_token


class DeleteCategory(Resource):

    @sensible_token
    def post(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        category_id = request.json["category_id"]
        user_id = decoded_token["user_id"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("delete from category where id=%s and customer_id=%s limit 1", (category_id, user_id))
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return jsonify(
            {
                "message": "categories will be deleted!"
            }
        )