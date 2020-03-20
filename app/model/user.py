from app import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.VARCHAR(8), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(32), nullable=False)
    email = db.Column(db.VARCHAR(64), nullable=False)
    ip = db.Column(db.VARCHAR(15), nullable=False, default="")
    enable = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, username: str, password: str, email: str, ip: str):
        self.username = username
        self.password = password
        self.email = email
        self.ip = ip

    def __repr__(self):
        return f"<USER {self.username} : {self.password} @ {self.ip}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
