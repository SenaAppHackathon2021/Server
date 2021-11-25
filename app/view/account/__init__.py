# blueprint와 flask_restful로 route 설정
from flask import Blueprint
import flask_restful
from flask_restful import Api

account_blueprint = Blueprint('account', __name__, url_prefix='/register')
account_api = Api(account_blueprint)

from .signup import Signup
account_api.add_resource(Signup, '/')

email_blueprint = Blueprint("Email", __name__, url_prefix='/email')
email_api = Api(email_blueprint)

from .email import Email
email_api.add_resource(Email, '/')

from .email import CheckEmail
email_api.add_resource(CheckEmail, '/check')

login_blueprint = Blueprint("Login", __name__, url_prefix="/login")
login_api = Api(login_blueprint)

from .login import Login
login_api.add_resource(Login, '/')