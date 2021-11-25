from app.extexsion import db

class BaseMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
