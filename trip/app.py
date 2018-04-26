"""主模块"""
import logging
import os

from flask import Flask
from flask_restful import Api

from .controller.foot_print import FootPrint
from .controller.session import Session
from .controller.trace import Trace
from .controller.user import User

LOGGER = logging.getLogger(__name__)
__FLASK_INSTANCE = Flask(__name__)
__API = Api(__FLASK_INSTANCE, prefix='/api')
__API.add_resource(User, '/users', '/users/<string:user_id>')
__API.add_resource(Session, '/sessions')
__API.add_resource(FootPrint, '/foot-prints',
                   '/foot-prints/<string:foot_print_id>')
__API.add_resource(Trace, '/traces', '/traces/<string:trace_id>')


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
