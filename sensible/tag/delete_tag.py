# SWAMI KARUPPASWAMI THUNNAI

import jwt
import graphene
from flask import request
from flask_graphql import GraphQLView
from user.helper import sensible_token
from database.get_connection import get_connection


class DeleteTag(graphene.Mutation):

    class Arguments:
        tag_list = graphene.List(graphene.Int, required=True)

    response = graphene.Int()
    message = graphene.Int()

    @staticmethod
    def mutate(root, info, tag_list):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            for tag in tag_list:
                cursor.execute("delete from tag where id=%s and user_id=%s limit 1", (tag, user_id))
                connection.commit()
        finally:
            cursor.close()
            connection.close()
        return DeleteTag(response=200, message="Tags will be deleted if the ID belongs to the user.")


class DeleteTagObjType(graphene.ObjectType):
    delete_tag = DeleteTag.Field()


def delete_tag_wrapper_function():
    view = GraphQLView.as_view("delete_tag", schema=graphene.Schema(mutation=DeleteTagObjType))
    return sensible_token(view)


