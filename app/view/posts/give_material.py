# 재료 요청 API 작성

import datetime
from flask import session, request, jsonify
from flask_restful import Resource
import random

from app.view import check_login
from app.model.posts.give_material import Material

class MaterialPost(Resource):
    def get(self):
        if check_login() == False:
            return "You need login", 401

        result_arr = []

        all_arts = Material.find_all_material_post()
        
        for i in range(0, len(all_arts)):
            result_arr.append({
                "post_id" : all_arts[i].post_id,
                "title" : all_arts[i].title,
                "requsetor" : all_arts[i].user_id,
                "created_time" : str(all_arts[i].creation_time),
                "picture" : all_arts[i].image
            })
        
        return result_arr, 200

    def post(self):
        if check_login() == False:
            return "You need login", 401

        json_request = request.json

        json_request['creation_time'] = datetime.datetime.now()
        json_request['post_id'] = random.randrange(0, 100000)
        json_request['user_id'] = session['user_id']

        Material.create_material_post(request.json)

        return "create post success", 200

class MaterialManage(Resource):
    def get(self, post_id):
        if check_login() == False:
            return "You need login", 401

        material_post = Material.find_one_material_post(post_id)

        result = {
            "title" : material_post[0].title,
            "content" : material_post[0].contents,
            "user" : material_post[0].user_id,
            "creation_time" : material_post[0].creation_time,
            "imgae" : material_post[0].image,
            "locatino" : material_post[0].location,
            "conttact" : material_post[0].contact
        }

        return result, 200

    def put(self, post_id):
        if check_login() == False:
            return "You need login", 401
        
        json_request = request.json
        user_id = session['user_id']

        if Material.update_material_post(json_request, post_id, user_id) == 400:
            return "modify post fail", 400
        elif Material.update_material_post(json_request, post_id, user_id) == 403:
            return "You are not author", 403

        return "modify post success", 200

    def delete(self, post_id):
        if check_login() == False:
            return "You need login", 401
            
        user_id = session['user_id']

        if Material.delete_material_post(post_id, user_id) == 500:
            return "delete post fail", 500
        elif Material.delete_material_post(post_id, user_id) == 403:
            return "You are not author", 403

        return "delete post success", 200