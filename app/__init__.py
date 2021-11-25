# create_app 함수로 Flask 인스턴스 리턴

from flask import Flask

def register_blueprint(app : Flask):
    from .view.posts import arts_blueprint
    app.register_blueprint(arts_blueprint)

def create_app():
    app = Flask(__name__)

    register_blueprint(app)

    return app