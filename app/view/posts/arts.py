# 정크 아트 게시판 API 작성
from flask import session, request
from flask_restful import Resource

from app.model.posts import arts
from app.view import check_login

class ArtPosts(Resource):
    def get(self):
        check_login()

        all_arts = arts.ArtPost.find_all_arts()

        return "Get", 200

    def post(self):
        json_request = request.json
        return "Post", 200