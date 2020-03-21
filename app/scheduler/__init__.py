from .handler import scheduler
from app import app


def initialize():
    scheduler.init_app(app)
    scheduler.start()
