# 정크 아트 게시판 API 작성
from flask import session
from flask_restful import Resource

from app.model.posts import arts

class ArtPosts(Resource):
    def get(self):
        check_login()

        all_arts = arts.ArtPost.find_all_arts()

        return "Get", 200

    def post(self):

        return "Post", 200

def check_login():
    try:
        with session['user']:
            pass
    except:
        return "You need login", 401