from functools import wraps

from flask import session

from app.handler.response import response_require_login
from app.model import User


def auth(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not is_logged_in():
            return response_require_login()
        return fn(*args, **kwargs)

    return wrapped


def log_in(user_id: int) -> None:
    session['uid'] = user_id
    session.permanent = True


def log_out():
    session.clear()


def is_logged_in() -> bool:
    return 'uid' in session


def get_user_id() -> int:
    return session['uid']


def get_user() -> User:
    uid = session['uid']
    return User.query.get(uid) if uid is not None else None
