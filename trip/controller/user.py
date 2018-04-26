"""用户控制器"""
import logging

from flask import request
from flask_restful import Resource, fields, marshal_with

from ..service import session, user

LOGGER = logging.getLogger(__name__)


class User(Resource):
    """ 用户资源 """
    user_fields = {
        'id': fields.String,
        'name': fields.String
    }

    @marshal_with(user_fields)
    def post(self):
        """ 用户注册 """
        json = request.get_json(force=True)
        user_name = json.get('user_name')
        password = json.get('password')
        return user.sign_up(user_name, password)

    @marshal_with(user_fields)
    def get(self, user_id):
        """ 获取用户信息 """
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            return user.get_by_id(user_id)
        else:
            return {}
