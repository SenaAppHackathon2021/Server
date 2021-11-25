# User 테이블 클래스와 메소드 작성
from app.extexsion import db
from app.view.account import email
from app.model.mixin import BaseMixin

class Account(db.Model, BaseMixin):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(15), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    picture = db.Column(db.String(45), nullable = False)

    def __init__(self, user_id, name, email, password, picture):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.picture = picture

    @staticmethod
    def signup(user_id, name, email, password):
        Account(
            user_id = user_id,
            name = name,
            email = email,
            password = password,
            picture = ""
        ).save()

    @staticmethod
    def login(email, password):
        user = Account.query.filter_by(email=email, password=password).all()

        if len(user) <= 0:
            return None, 400
        else:
            return user[0].user_id, 200

    @staticmethod
    def find_profile(user_id):
        return Account.query.filter_by(user_id=user_id).all()
        