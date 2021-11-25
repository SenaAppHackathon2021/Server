# 재료 요청 API 작성

import datetime
from flask import session, request, jsonify
from flask_restful import Resource
import random

from app.view import check_login
from app.model.posts.give_material import Material

class MaterialPost(Resource):
    def get(self):
        check_login()

        result_arr = []

        all_arts = Material.find_all_material_post()
        
        for i in range(0, len(all_arts)):
            result_arr.append({
                "post_id" : all_arts[i].post_id,
                "title" : all_arts[i].title,
                "requsetor" : all_arts[i].user_id, # 유저 테이블이 만들어지기 전 임시
                "created_time" : str(all_arts[i].creation_time),
                "picture" : all_arts[i].image
            })
        
        return result_arr, 200