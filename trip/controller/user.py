"""用户控制器"""
import logging

from flask import request
from flask_restful import Resource, marshal_with, fields

from ..service import user

LOGGER = logging.getLogger(__name__)


class User(Resource):
    user_fields = {
        'id': fields.String,
        'name': fields.String
    }

    @marshal_with(user_fields)
    def post(self):
        json = request.get_json(force=True)
        user_name = json.get('user_name')
        password = json.get('password')
        return user.sign_up(user_name, password)
