"""主模块"""
import logging
import os

from flask import Flask
from flask_restful import Api

from .controller import foot_print, session, trace, user, foot_print_list

LOGGER = logging.getLogger(__name__)
__FLASK_INSTANCE = Flask(__name__)
__API = Api(__FLASK_INSTANCE, prefix='/api')
__API.add_resource(user.User, '/users', '/users/<string:user_id>')
__API.add_resource(session.Session, '/sessions', '/sessions/<string:session_id>')
__API.add_resource(foot_print.FootPrint, '/foot-prints',
                   '/foot-prints/<string:foot_print_id>')
__API.add_resource(trace.Trace, '/traces', '/traces/<string:trace_id>')
__API.add_resource(foot_print_list.FootPrintList, '/foot-print-lists')


@__FLASK_INSTANCE.route('/api', methods=['GET'])
def root():
    """主页"""
    return 'Welcome to Trip API! https://github.com/yzyzt/trip-backend.git\r\n'


def run(debug=False, host='localhost', port=8005):
    """运行"""
    LOGGER.info('trip启动')
    __FLASK_INSTANCE.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    LOGGER.info('PID=%d', os.getpid())
    run()
