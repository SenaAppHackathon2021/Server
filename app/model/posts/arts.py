# 정크 아트 게시글 테이블 클래스와 메소드 작성
from sqlalchemy.orm import backref
from app.extension import db

class ArtPost(db.Model):
    __tablename__ = "art_post"

    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    contents = db.Column(db.String(300))
    sponsor = db.Column(db.String(500))
    before_img = db.Column(db.String(45), nullable=False)
    after_img = db.Column(db.String(45), nullable=False)
    creation_time = db.Column(db.DateTime(), nullable=False)

    def __init__(self, post_id, user_id, title, contents, sponsor, before_img, after_img, creation_time):
        self.post_id= post_id
        self.user_id = user_id
        self.title = title
        self.contents = contents
        self.sponsor = sponsor
        self.before_img = before_img
        self.after_img = after_img
        self.creation_time = creation_time


    @staticmethod
    def find_all_arts():
        return ArtPost.query.filter_by().all()

    @staticmethod
    def create_art_post():
        return "create"