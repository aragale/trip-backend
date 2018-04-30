""" 路途控制器 """
from flask import request
from flask_restful import Resource, fields, marshal_with

from ..service import session, trace


class Trace(Resource):
    trace_fields = {
        'id': fields.String,
        'positions': fields.Raw
    }

    @marshal_with(trace_fields)
    def post(self):
        """ 创建路途 """
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            json = request.get_json(force=Trace)
            return trace.create(json)
        else:
            return None
    
    @marshal_with(trace_fields)
    def get(self, trace_id):
        session_id = request.headers.get('session')
        if session.is_valid(session_id):
            return trace.get(trace_id)
        else:
            return None
