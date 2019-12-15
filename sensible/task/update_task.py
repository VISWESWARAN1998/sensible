# SWAMI KARUPPASWAMI THUNNAI

import jwt
import graphene
from flask import request
from flask_graphql import GraphQLView
from task.task_model import TaskModel
from sqlalchemy.orm import sessionmaker
from database.get_connection import orm_connection
from graph_helper.camel_to_snake import camel_to_snake
from user.helper import sensible_token


class UpdateTask(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(description="The name of the task")
        category_id = graphene.Int()
        due_date = graphene.Date(description="The date for which the task is in due")
        due_time = graphene.Time(description="The time for which the task is in due")
        completed_date = graphene.Date(description="The date in which the task has been completed.")
        completed_time = graphene.Time(description="The time in which the project has been completed.")
        opportunity_id = graphene.Int(description="Assign the task to an opportunity.")
        status = graphene.Int(description="The status of a task. 0 for open 1 for working 3 for completed.")

    message = graphene.String(description="The message which will be returned")

    @staticmethod
    def mutate(root, info, **kwargs):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        payload = kwargs
        _id = payload["id"]
        engine = orm_connection()
        _session = sessionmaker(bind=engine)
        session = _session()
        for i in payload:
            column_name = camel_to_snake(i)
            if column_name != "id":
                session.query(TaskModel).filter(TaskModel.user_id == user_id).update({column_name: payload[i]})
                session.commit()
        return UpdateTask(message="DONE!")


class UpdateObjType(graphene.ObjectType):

    update_task = UpdateTask.Field()


def update_task_wrapper():
    view = GraphQLView.as_view("update_task", schema=graphene.Schema(mutation=UpdateObjType), graphiql=True)
    return sensible_token(view)