from flask import request

from app import app
from app.handler.auth import log_in, log_out, auth, get_user
from app.handler.request import json_required
from app.handler.response import response_invalid_request, response_msg, response_duplicated_user, response_no_record, \
    response_require_login, response_data, response_internal_error
from app.model import User


@app.route('/api/user/register', methods=['POST'])
@json_required
def api_user_register():
    try:
        json = request.json

        if "username" not in json or "password" not in json or "email" not in json or "ip" not in json:
            return response_invalid_request()

        new_user = User(json["username"], json["password"], json["email"], json["ip"])
        new_user.save()
        if not new_user.id > 0:
            return response_duplicated_user()

        log_in(new_user.id)
        return response_msg(0, "register successfully", 200)
    except Exception:
        return response_internal_error()


@app.route('/api/user/login', methods=['POST'])
@json_required
def api_user_login():
    try:
        json = request.json

        if "username" not in json or "password" not in json:
            return response_invalid_request()

        user = User.query.filter(User.username == json["username"], User.password == json["password"]).one_or_none()
        if user is None:
            return response_no_record()

        log_in(user.id)
        return response_msg(0, "login successfully", 200)
    except Exception:
        return response_internal_error()


@app.route('/api/user/logout', methods=['GET'])
def api_user_logout():
    log_out()
    return response_msg(0, "logout successfully", 200)


@app.route('/api/user/info', methods=['GET'])
@auth
def api_user_get_info():
    try:
        user = get_user()
        if user is None:
            return response_require_login()

        return response_data(0, {
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "ip": user.ip,
            "enable": user.enable,
        }, 200)
    except Exception:
        return response_internal_error()


@app.route('/api/user/info', methods=['POST'])
@auth
@json_required
def api_user_update_info():
    try:
        user = get_user()
        if user is None:
            return response_require_login()

        json = request.json

        if "username" in json:
            user.username = json["username"]

        if "password" in json:
            user.password = json["password"]

        if "email" in json:
            user.email = json["email"]

        if "ip" in json:
            user.ip = json["ip"]

        if "enable" in json:
            user.enable = json["enable"]

        user.update()

        return response_msg(0, "update successfully", 200)
    except Exception:
        return response_internal_error()
