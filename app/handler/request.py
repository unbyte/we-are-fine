from functools import wraps

from flask import request

from app.handler.response import response_invalid_request


def json_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if request.json is None:
            return response_invalid_request()
        return fn(*args, **kwargs)

    return wrapped
