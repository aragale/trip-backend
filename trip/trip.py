"""主模块"""
import logging

from flask import Flask
from flask_restful import Api

from .controller.user import User

LOGGER = logging.getLogger(__name__)
__FLASK_INSTANCE = Flask(__name__)
__API = Api(__FLASK_INSTANCE, prefix='/api')
__API.add_resource(User, '/users')


@__FLASK_INSTANCE.route('/api', methods=['GET'])
def root():
    """主页"""
    return 'Welcome to Trip API! https://github.com/yzyzt/trip-backend.git'


def run(debug=False, host='127.0.0.1', port=9000):
    LOGGER.info('trip启动')
    __FLASK_INSTANCE.run(debug=debug, host=host, port=port)
