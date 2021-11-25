# create_app 함수로 Flask 인스턴스 리턴

from flask import Flask, config
import config

def register_extension(app : Flask):
    from app import extension
    extension.db.init_app(app)

def register_blueprint(app : Flask):
    from .view.posts import arts_blueprint
    app.register_blueprint(arts_blueprint)

def create_app():
    app = Flask(__name__)

    app.secret_key = "1234"
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    register_blueprint(app)
    register_extension(app)

    return app