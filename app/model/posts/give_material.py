# 재료 요청 게시글 테이블 클래스와 메소드 작성
from os import stat
from app.extension import db
from app.model.mixin import BaseMixin

class Material(db.Model, BaseMixin):
    __tablename__ = "request_post"

    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    contents = db.Column(db.String(300))
    contact = db.Column(db.String(40))
    location = db.Column(db.String(45), nullable=False)
    image = db.Column(db.String(45), nullable=False)
    creation_time = db.Column(db.DateTime(), nullable=False)

    def __init__(self, post_id, user_id, title, contents, contact, location, image, creation_time):
        self.post_id= post_id
        self.user_id = user_id
        self.title = title
        self.contents = contents
        self.contact = contact
        self.location = location
        self.image = image
        self.creation_time = creation_time

    @staticmethod
    def find_all_material_post():
        return Material.query.filter_by().all()