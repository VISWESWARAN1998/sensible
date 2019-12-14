# SWAMI KARUPPASWAMI THUNNAI

from flask import Flask
from flask_restful import Api

# Public resources which doesn't need any tokens
from public.get_currency_list import CurrencyList

# User account related imports
from user.signup import UserSignup
from user.login import UserLogin

# Tags for user
from tag.add_tag import add_tag_wrapper
from tag.delete_tag import delete_tag_wrapper_function
from tag.my_tag import MyTag

# Category related imports
from category.add_category import AddCategory
from category.my_category import MyCategory
from category.delete_category import DeleteCategory

# Tasks related imports
from task.add_task import AddTask

app = Flask(__name__)
api = Api(app=app)

# Public resources
api.add_resource(CurrencyList, "/currency_list")

# user related resources
api.add_resource(UserSignup, "/user_signup")
api.add_resource(UserLogin, "/user_login")

# Tags
app.add_url_rule("/add_tag", view_func=add_tag_wrapper())
app.add_url_rule("/delete_tag", view_func=delete_tag_wrapper_function())
api.add_resource(MyTag, "/my_tag_list")

# Categories
api.add_resource(AddCategory, "/add_category")
api.add_resource(MyCategory, "/my_category_list")
api.add_resource(DeleteCategory, "/delete_category")

# Tasks
api.add_resource(AddTask, "/add_task")


if __name__ == "__main__":
    app.run(debug=True)