# blueprint와 flask_restful로 route 설정
from flask import Blueprint
from flask_restful import Api

arts_blueprint = Blueprint('arts', __name__, url_prefix='/arts')
arts_api = Api(arts_blueprint)

from .arts import ArtPosts, ManageArt
arts_api.add_resource(ArtPosts, '/')
arts_api.add_resource(ManageArt, '/<post_id>')

material_blueprint = Blueprint('material', __name__, url_prefix='/material')
material_api = Api(material_blueprint)

from .give_material import MaterialPost
material_api.add_resource(MaterialPost, '/')