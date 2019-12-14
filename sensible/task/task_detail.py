# SWAMI KARUPPASWAMI THUNNAI

import graphene


class TaskDetail(graphene.ObjectType):

    task_id = graphene.ID(description="The unique id of a task")
    user_id = graphene.Int(description="The id of an user to which the task has been assigned")
    name = graphene.String(description="The name of the task.")
    category_id = graphene.Int(description="The category of the task. Example: Call, Email")
    due_date = graphene.Date(ddescription="The due date for the task")
    due_time = graphene.Time(description="The due time for the task")
    completed_date = graphene.Date(description="The date in which the task has been completed.")
    completed_time = graphene.Time(descripton="The time in which the task has been completed.")
    opportunity_id = graphene.Int(description="This is an optional parameter")
    status = graphene.Int(description="The status of the task. 0 -> Not completed; 1-> Working; 2->Completed.")


class TaskDetailQuery(graphene.ObjectType):

    task_detail_list = graphene.Field(graphene.List(TaskDetail), args={"id_list": graphene.List(graphene.Int)})
