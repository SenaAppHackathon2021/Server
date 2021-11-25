from flask import Flask

def register_extension(app : Flask):
    from .extexsion import db
    extexsion.db.init_app(app)

def register_blueprint(app : Flask):
    from .view.account import account_blueprint
    app.register_blueprint(account_blueprint)

def create_app():
    app = Flask(__name__)

    register_blueprint(app)
    register_extension(app)

    return app