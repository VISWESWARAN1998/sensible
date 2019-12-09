# SWAMI KARUPPASWAMI THUNNAI

from flask_restful import Resource
from user.helper import sensible_token


class TestR(Resource):

    @sensible_token
    def get(self):
        return "Hello World!"