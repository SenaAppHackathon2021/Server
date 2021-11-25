# 회원가입 관련 API 작성
from flask import json, request, jsonify
from flask_restful import Resource
from app.model.account import Account

class Signup(Resource):
    def post(self):
        id = request.json['id']
        password = request.json['password']
        email = request.json['email']
        try:
            Account.signup(id, password, email)
        except:
            return jsonify({"message" : "account create fail", "status_code" : "400"}})

        return jsonify({"message" : "account created", "status_code" : "201"})