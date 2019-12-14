# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from user.helper import sensible_token
from database.get_connection import get_connection


class AddCategory(Resource):

    @sensible_token
    def post(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        category_name = request.json["category_name"]
        hex_color = request.json["hex_color"]
        hex_color = hex_color.strip()
        category_name = category_name.strip()
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id from category where name=%s and customer_id=%s limit 1", (category_name, user_id))
            result = cursor.fetchone()
            if result is None:
                cursor.execute("insert into category value(null, %s, %s, %s)", (user_id, category_name, hex_color))
                connection.commit()
        finally:
            cursor.close()
            connection.close()
        return jsonify(
            {
                "message": "Category has been added!"
            }
        )