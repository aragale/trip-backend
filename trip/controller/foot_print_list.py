""" 足迹列表控制器 """

import logging
from flask import request
from flask_restful import Resource, fields, marshal_with

from ..service import session, foot_print_list
from ..controller import foot_print

class FootPrintList(Resource):
    @marshal_with(foot_print.FootPrint.foot_print_fields)
    def get(self):
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            return foot_print_list.get(request.args.get('user_id'))
        else:
            return []
