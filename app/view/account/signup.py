# 회원가입 관련 API 작성
from flask import json, request, jsonify
from flask_restful import Resource
from app.model.account import Account
from random import *

class Signup(Resource):
    def post(self):
        id = request.json['id']
        password = request.json['password']
        email = request.json['email']
        user_id = randint(10000, 99999)
        print(user_id, id, password, email)
        
        Account.signup(user_id, id, password, email)
        
        return jsonify({"message" : "account created", "status_code" : "201"})