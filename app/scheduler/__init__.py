import logging
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from app import app
from flask_apscheduler import APScheduler

from app.notifier import sender
from app.scheduler.handler import sign_all

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='run.log',
                    filemode='a')


def initialize():
    # 计划任务
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(id="main", func=sign_all, trigger='cron', second='0 8-16/2 * * *')
    scheduler._logger = logging
    scheduler.add_listener(lambda event: sender.alert("计划任务出错", str(event)), EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()
