import logging
import time
from typing import List

from apscheduler.events import EVENT_JOB_ERROR
from flask_apscheduler import APScheduler

from app import db
from app.model import User, Record
from app.notifier import get_notifier, Notifier, alert
from app.scheduler.job import Job

scheduler = APScheduler()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='run.log',
                    filemode='a')

scheduler._logger = logging
scheduler.add_listener(lambda event: alert("计划任务出错", str(event)), EVENT_JOB_ERROR)


@scheduler.task('cron', id='main', second='0', minute='0', hour='8-16/2', day='*', month='*', year='*')
def sign_all():
    today: int = int(time.time()) - int(time.time() - time.timezone) % 86400
    users: List[User] = db.session.query(User).filter(~User.id.in_(
        db.session.query(User.id).join(Record, Record.user_id == User.id)
            .filter(Record.time >= today)
            .filter(Record.success)
            .subquery()
    )).filter(User.enable).all()
    if len(users) == 0:
        return

    sender = get_notifier()
    for user in users:
        sign(user, sender)
        time.sleep(1)
    sender.disconnect()


def sign(user: User, sender: Notifier) -> None:
    success, title, info = Job(user.username, user.password, user.ip).do()
    try:
        sender.send(user.email, title, info)
    except Exception:
        info += "\n通知邮件发送失败"

    try:
        Record(user.id, success, f"{title}\n{info}", int(time.time())).save()
    except Exception:
        db.session.rollback()
