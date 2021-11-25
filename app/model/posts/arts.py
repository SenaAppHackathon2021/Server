# 정크 아트 게시글 테이블 클래스와 메소드 작성
from app.extension import db

class ArtPost(db.Model):
    __tablename__ = "Art_post"

    @staticmethod
    def find_all_arts():
        return "Hello"