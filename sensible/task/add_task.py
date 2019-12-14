# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from user.helper import sensible_token
from database.get_connection import get_connection
from sensible_exception import SensibleException


class AddTask(Resource):

    @sensible_token
    def post(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        name = request.json["name"]
        category_id = request.json["category_id"]
        due_date = request.json["due_date"]
        due_time = request.json["due_time"]
        status = request.json["status"]
        try:
            opportunity_id = request.json["opportunity"]
        except KeyError:
            opportunity_id = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select name from category where id=%s and customer_id=%s limit 1", (category_id, user_id))
            result = cursor.fetchone()
            if result is None:
                return SensibleException.raise_exception(SensibleException.DATA_NOT_PRESENT)
            if opportunity_id:
                cursor.execute("insert into task value(null, %s, %s, %s, %s, %s, null, null, %s, %s)", (
                    user_id, name, category_id, due_date, due_time, opportunity_id, status
                ))
            else:
                cursor.execute("insert into task value(null, %s, %s, %s, %s, %s, null, null, null, %s)", (
                    user_id, name, category_id, due_date, due_time, status
                ))
            connection.commit()
            return jsonify(
                {
                    "message": "Task has been added!"
                }
            )
        finally:
            cursor.close()
            connection.close()
