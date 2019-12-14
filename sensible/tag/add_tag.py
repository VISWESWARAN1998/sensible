# SWAMI KARUPPASWAMI THUNNAI

import graphene
import jwt
from flask import request
from database.get_connection import get_connection
from flask_graphql import GraphQLView
from user.helper import sensible_token


class TagDetail(graphene.InputObjectType):
    tag_name = graphene.String()

class AddTag(graphene.Mutation):

    class Arguments:
        tag_list = graphene.List(TagDetail, required=True)
    response = graphene.Int()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, tag_list):
        access_token = request.headers["x-access-token"]
        decoded_token = jwt.decode(access_token, verify=False)
        user_id = decoded_token["user_id"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            for tag in tag_list:
                tag_name = tag["tag_name"]
                cursor.execute("select id from tag where name=%s and user_id=%s limit 1", (tag_name, user_id))
                result = cursor.fetchone()
                if result is None:
                    cursor.execute("insert into tag value(null, %s, %s)", (user_id, tag_name))
                    connection.commit()
        finally:
            cursor.close()
            connection.close()
        return AddTag(response=200, message="Tags have been added!")


class AddTagObjType(graphene.ObjectType):
    tag_detail = AddTag.Field()


def add_tag_wrapper():
    view = GraphQLView.as_view("add_tag", schema=graphene.Schema(mutation=AddTagObjType))
    return sensible_token(view)



