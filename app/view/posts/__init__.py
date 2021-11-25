# blueprint와 flask_restful로 route 설정
from flask import Blueprint
from flask_restful import Api

arts_blueprint = Blueprint('arts', __name__, url_prefix='/arts')
arts_api = Api(arts_blueprint)

from .arts import ArtPosts
arts_api.add_resource(ArtPosts, '/')