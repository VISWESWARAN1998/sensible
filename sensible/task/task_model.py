# SWAMI KARUPPASWAMI THUNNAI

import sqlalchemy
from database.get_connection import Base


class TaskModel(Base):

    __tablename__ = "task"

    id = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    category_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False)
    due_date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    due_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False)
    completed_date = sqlalchemy.Column(sqlalchemy.Date)
    completed_time = sqlalchemy.Column(sqlalchemy.Time)
    opportunity_id = sqlalchemy.Column(sqlalchemy.BIGINT)
    status = sqlalchemy.Column(sqlalchemy.INT, nullable=False, default=0)


def get_column_names(fields):
    column_names = []
    for field in fields:
        column_name = ""
        for character in field:
            if character.isupper():
                column_name += "_"
                column_name += character.lower()
            else:
                column_name += character
        column_names.append(column_name)
    return column_names
