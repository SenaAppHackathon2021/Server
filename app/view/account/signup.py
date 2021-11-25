# 회원가입 관련 API 작성
from flask import request, jsonify
from flask_restful import Resource

class Signup(Resource):
    def post(self):
        id = request.json['id']
        password = request.json['password']
        email = request.json['email']
        return 