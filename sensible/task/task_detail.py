# SWAMI KARUPPASWAMI THUNNAI

import jwt
import graphene
import sqlalchemy
from flask import request
from graph_helper.ast_to_dict import get_fields
from flask_graphql import GraphQLView
from task.task_model import TaskModel, get_column_names
from database.get_connection import orm_connection
from sqlalchemy.orm import sessionmaker, load_only
from user.helper import sensible_token
from graph_helper.alchemy_obj_to_args import obj_to_args


class TaskDetail(graphene.ObjectType):

    id = graphene.ID(description="The unique id of a task")
    user_id = graphene.Int(description="The id of an user to which the task has been assigned")
    name = graphene.String(description="The name of the task.")
    category_id = graphene.Int(description="The category of the task. Example: Call, Email")
    due_date = graphene.Date(description="The due date for the task")
    due_time = graphene.Time(description="The due time for the task")
    completed_date = graphene.Date(description="The date in which the task has been completed.")
    completed_time = graphene.Time(description="The time in which the task has been completed.")
    opportunity_id = graphene.Int(description="This is an optional parameter")
    status = graphene.Int(description="The status of the task. 0 -> Not completed; 1-> Working; 2->Completed.")


class TaskDetailQuery(graphene.ObjectType):

    task_detail_list = graphene.Field(graphene.List(TaskDetail), args={"id_list": graphene.List(graphene.Int)})

    @staticmethod
    def resolve_task_detail_list(root, info, id_list):
        decoded_token = jwt.decode(request.headers["x-access-token"], verify=False)
        user_id = decoded_token["user_id"]
        response = []
        fields = get_fields(info)
        column_names = get_column_names(fields)
        engine = orm_connection()
        _session = sessionmaker(bind=engine)
        session = _session()
        for _id in id_list:
            result = session.query(TaskModel).options(load_only(*column_names)).filter(sqlalchemy.and_(
                TaskModel.id == _id,
                TaskModel.user_id == user_id
            ))
            result = result.first()
            if result:
                args = obj_to_args(result)
                response.append(TaskDetail(**args))
        return response


def task_detail_wrapper():
    view = GraphQLView.as_view("task_detail", schema=graphene.Schema(query=TaskDetailQuery), graphiql=True)
    return sensible_token(view)
