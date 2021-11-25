# 정크 아트 게시판 API 작성
import datetime
from flask import json, session, request, jsonify
from flask_restful import Resource
import random

from app.model.posts import arts
from app.view import check_login

class ArtPosts(Resource):
    def get(self):
        check_login()

        result_arr = []

        all_arts = arts.ArtPost.find_all_arts()
        
        
        for i in range(0, len(all_arts)):
            result_arr.append({
                "post_id" : all_arts[i].post_id,
                "title" : all_arts[i].title,
                "artist" : all_arts[i].user_id, # 유저 테이블이 만들어지기 전 임시
                "created_time" : str(all_arts[i].creation_time),
                "picture" : all_arts[i].after_img
            })
        
        return result_arr, 200

    def post(self):
        json_request = request.json

        json_request['creation_time'] = datetime.datetime.now()
        json_request['post_id'] = random.randrange(0, 100000)
        json_request['user_id'] = session['user_id']

        arts.ArtPost.create_art_post(json_request)

        return "create post success", 200