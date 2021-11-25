from flask_restful import Resource
from flask import session

from app.model.account import Account
from app.model.posts.arts import ArtPost

class ProfilePage(Resource):
    def get(self):
        try:
            user_id = session['user_id']
        except:
            return "You need login", 401

        user_info = Account.find_profile(user_id)
        posts = ArtPost.find_my_arts(user_id)

        posts_list = []

        for i in range(0, len(posts)):
            posts_list.append({
                "post_id" : posts[i].post_id,
                "image" : posts[i].after_img
            })

        result = [{
            "profile" : user_info[0].picture,
            "name" : user_info[0].name,
            "email" : user_info[0].email,
            "post" : posts_list
        }]
        

        return result, 200