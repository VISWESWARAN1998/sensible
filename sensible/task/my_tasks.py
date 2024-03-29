# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from user.helper import sensible_token


class MyTasks(Resource):

    @sensible_token
    def get(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id from task where user_id=%s", (user_id, ))
            task_list = cursor.fetchall()
            cursor.execute("select count(id) as not_completed from task where status!=2 and user_id=%s", (user_id, ))
            not_completed = cursor.fetchone()["not_completed"]
            return jsonify(
                {
                    "task_list": task_list,
                    "not_completed": not_completed
                }
            )
        finally:
            cursor.close()
            connection.close()