# SWAMI KARUPPASWAMI THUNNAI

import jwt
from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from user.helper import sensible_token


class NewOrganization(Resource):

    @sensible_token
    def post(self):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        name = request.json["name"]
        address = request.json["address"]
        website = request.json["website"]
        country_code = request.json["country_code"]
        phone = request.json["phone"]
        twitter = request.json["twitter"]
        facebook = request.json["facebook"]
        linkedin = request.json["linkedin"]
        instagram = request.json["instagram"]
        image = request.json["image"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("insert into organization value(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (
                               user_id, name, address, website, country_code, phone, twitter, facebook, linkedin,
                               instagram, image
                           ))
            connection.commit()
        finally:
            cursor.close()
            connection.close()
        return jsonify(
            {
                "message": "Organization has been added!"
            }
        )