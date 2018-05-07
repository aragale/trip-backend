import logging

from flask import request
from flask_restful import Resource, fields, marshal_with

from ..service import session

LOGGER = logging.getLogger(__name__)


class Session(Resource):
    session_fields = {
        'user_id': fields.String,
        'time': fields.DateTime(dt_format='iso8601')
    }

    @marshal_with(session_fields)
    def get(self):
        """获取会话"""
        session_id = request.headers.get('session')
        return session.get(session_id)

    def post(self):
        """登入"""
        json = request.get_json(force=True)
        user_name = json.get('user_name')
        password = json.get('password')
        return session.sign_in(user_name, password)

    def delete(self, session_id):
        """登出"""
        return session.sign_out(session_id)
