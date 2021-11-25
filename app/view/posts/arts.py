# 정크 아트 게시판 API 작성
from flask_restful import Resource

class ArtPosts(Resource):
    def get(self):
        return "Get", 200

    def post(self):
        return "Post", 200