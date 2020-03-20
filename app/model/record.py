from app import db


class Record(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    success = db.Column(db.Boolean, nullable=False, default=False, index=True)
    info = db.Column(db.VARCHAR(128), nullable=False, default="")
    time = db.Column(db.Integer, nullable=False, index=True)

    def __init__(self, user_id: int, success: bool, info: str, time: int):
        self.user_id = user_id
        self.success = success
        self.info = info
        self.time = time

    def __repr__(self):
        return f"<RECORD success({self.success}) by {self.user_id} @ time({self.time}) : {self.info}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
