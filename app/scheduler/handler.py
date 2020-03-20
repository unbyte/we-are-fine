import time
from typing import List

from app import db
from app.model import User, Record
from app.notifier import sender
from app.scheduler.job import Job


def sign_all():
    today: int = int(time.time()) - int(time.time() - time.timezone) % 86400
    users: List[User] = db.session.query(User).filter(~User.id.in_(
        db.session.query(User.id).join(Record, Record.user_id == User.id)
            .filter(Record.time >= today)
            .filter(Record.success)
            .subquery()
    )).filter(User.enable).all()

    for user in users:
        sign(user)
        time.sleep(1)


def sign(user: User) -> None:
    success, info = Job(user.username, user.password, user.ip).do()

    Record(user.id, success, info, int(time.time())).save()

    sender.send(user.email, "打卡成功" if success else "打卡失败", info)
