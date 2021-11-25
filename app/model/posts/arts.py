# 정크 아트 게시글 테이블 클래스와 메소드 작성
from app.extension import db
from app.model.mixin import BaseMixin

class ArtPost(db.Model, BaseMixin):
    __tablename__ = "art_post"

    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
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
    def create_art_post(request : dict):
        ArtPost(
            title=request['title'],
            contents=request['content'],
            before_img=request['picture']['before'],
            after_img=request['picture']['before'],
            sponsor=request['sponsor'],
            post_id=request['post_id'],
            user_id=request['user_id'],
            creation_time=request['creation_time']
        ).save()

    @staticmethod
    def update_art_post(request : dict, post_id):
        select_db = ArtPost.query.filter_by(post_id=post_id).all()

        try:
            select_db[0].title = request['title']
            select_db[0].contents = request['content']
            select_db[0].before_img = request['picture']['before']
            select_db[0].after_img=request['picture']['before']
            select_db[0].sponsor=request['sponsor']

            db.session.commit()
        except:
            return False

        return True