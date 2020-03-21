from app import app
from app.handler.auth import auth, get_user, get_user_id
from app.handler.response import response_require_login, response_data, response_internal_error
from app.model import Record


@app.route('/api/record/list', methods=['GET'])
@auth
def api_record_list():
    """
    GET /api/record/list

    success: 200 {code:0, data:[{time, success, info}]}
    """
    try:
        records = Record.query.filter(Record.user_id == get_user_id()).all()

        return response_data(0, [{
            "time": record.time,
            "success": record.success,
            "info": record.info
        } for record in records], 200)

    except Exception:
        return response_internal_error()
