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

    @staticmethod
    def create_material_post(request : dict):
        Material(
            title=request['title'],
            contents=request['content'],
            image=request['image'],
            location=request['location'],
            contact=request['contact'],
            post_id=request['post_id'],
            user_id=request['user_id'],
            creation_time=request['creation_time']
        ).save()

    @staticmethod
    def update_material_post(request : dict, post_id, user_id):
        select_db = Material.query.filter_by(post_id=post_id).all()

        try:
            if select_db[0].user_id != user_id:
                return 403

            select_db[0].title = request['title']
            select_db[0].contents = request['content']
            select_db[0].image = request['image']

            db.session.commit()
        except:
            return 400

        return True

    @staticmethod
    def delete_material_post(post_id, user_id):
        select_db = Material.query.filter_by(post_id=post_id).all()

        try:
            if select_db[0].user_id != user_id:
                return 403

            db.session.delete(select_db[0])
            db.session.commit()

        except:
            return 500

        return True