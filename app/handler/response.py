from flask import jsonify


def response_msg(code: int, msg: str, http_code: int) -> tuple:
    return jsonify({"code": code, "msg": msg}), http_code


def response_data(code: int, data: any, http_code: int) -> tuple:
    return jsonify({"code": code, "data": data}), http_code


def response_no_record() -> tuple:
    return response_msg(1, "not found", 404)


def response_no_permission() -> tuple:
    return response_msg(2, "no permission", 403)


def response_require_login() -> tuple:
    return response_msg(3, "login required", 401)


def response_invalid_request() -> tuple:
    return response_msg(4, "bad request", 400)


def response_duplicated_user() -> tuple:
    return response_msg(5, "duplicated user", 409)


def response_internal_error() -> tuple:
    return response_msg(-1, "internal error", 500)
