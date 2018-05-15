""" 足迹控制器 """
from flask import request
from flask_restful import Resource, fields, marshal_with

from ..service import foot_print, session


class FootPrint(Resource):
    """ 足迹资源类 """
    foot_print_fields = {
        'id': fields.String,
        'title': fields.String,
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

    @marshal_with(foot_print_fields)
    def get(self, foot_print_id):
        """ 获取足迹 """
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            return foot_print.get(foot_print_id)
        else:
            return None

    @marshal_with(foot_print_fields)
    def put(self, foot_print_id):
        """ 修改足迹 """
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            json = request.get_json(force=True)
            return foot_print.update(foot_print_id, json)
        else:
            return None

    def delete(self, foot_print_id):
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            return foot_print.delete(foot_print_id)
        else:
            return False