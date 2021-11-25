# create_app 함수로 Flask 인스턴스 리턴
from flask import Flask, config, session
from datetime import timedelta
from flask_mail import Mail, Message
from config import mail_pw, secret_key, db, DB_URL

def register_extension(app : Flask):
    from app import extension
    extension.db.init_app(app)
    extension.mail.init_app(app)
    
def register_blueprint(app : Flask):

    from .view.account import account_blueprint, email_blueprint, login_blueprint, logout_blueprint, profile_blueprint
    app.register_blueprint(account_blueprint)
    app.register_blueprint(email_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(profile_blueprint)
    
    from .view.posts import arts_blueprint, material_blueprint
    app.register_blueprint(arts_blueprint)
    app.register_blueprint(material_blueprint)

def create_app():
    app = Flask(__name__)
    app.permanent_session_lifetime = timedelta(minutes=1)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'reart.senaapp@gmail.com'
    app.config['MAIL_PASSWORD'] = mail_pw
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['SECRET_KEY'] = secret_key
    
    app.config['SESSION_TYPE'] = 'filesystem'

    app.secret_key = "1234"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    register_blueprint(app)
    register_extension(app)

    return app