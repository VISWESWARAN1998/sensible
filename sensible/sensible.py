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

app = Flask(__name__)
api = Api(app=app)

# Public resources
api.add_resource(CurrencyList, "/currency_list")

# user related resources
api.add_resource(UserSignup, "/user_signup")
api.add_resource(UserLogin, "/user_login")

# Tags
app.add_url_rule("/add_tag", view_func=add_tag_wrapper())


if __name__ == "__main__":
    app.run(debug=True)