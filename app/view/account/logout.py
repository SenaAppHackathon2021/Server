# 로그인 및 로그 아웃 API 작성
from flask_restful import Resource
from flask import request, session

from app.model.account import Account
from app.view import check_login

class LogOut(Resource):
    def post(self):
        if check_login() == False:
            return "You need login", 401
        
        try:
            session.pop("user_id", None)

            return "logout success", 200
        except:
            return "logout fail", 400