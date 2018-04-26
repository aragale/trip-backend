""" 足迹控制器 """
from flask import request
from flask_restful import Resource, fields, marshal_with

from ..service import session, foot_print


class FootPrint(Resource):
    """ 足迹资源类 """
    foot_print_fields = {
        'id': fields.String,
        'title': fields.String,
        'user_id': fields.String,
        'time': fields.DateTime(dt_format='iso8601'),
        'description': fields.String,
        'images': fields.Raw,
        'trace_id': fields.String
    }

    @marshal_with(foot_print_fields)
    def post(self):
        """ 创建足迹 """
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            user_id = session.get_user_id_by_id(session_id)
            json = request.get_json(force=True)
            return foot_print.create(json, user_id)
        else:
            return None
