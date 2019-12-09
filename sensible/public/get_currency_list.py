# SWAMI KARUPPASWAMI THUNNAI

from flask import jsonify
from flask_restful import Resource
from database.get_connection import get_connection


class CurrencyList(Resource):

    def get(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id, name, symbol from currency")
            result = cursor.fetchall()
            return jsonify(
                {
                    "currency_detail": result
                }
            )
        finally:
            cursor.close()
            connection.close()