# 로그인 및 로그 아웃 API 작성
from flask_restful import Resource
from flask import request, session

from app.model.account import Account

class Login(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']

        user_info, status_code = Account.login(email, password)

        if status_code == 400:
            return "login fail", 400
        elif status_code == 200:
            session['user_id'] = user_info
            return "login success", 200