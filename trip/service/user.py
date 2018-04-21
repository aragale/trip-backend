"""用户逻辑模块"""
import hashlib
import logging
import uuid

from flask_restful import abort

from ..data import get_session
from ..models import User

LOGGER = logging.getLogger(__name__)


def sign_up(user_name, password) -> User:
    """用户注册"""
    if user_name is None or password is None:
        # 信息不完整
        abort(400, error='Incomplete information')
    # 获取会话
    sess = get_session()
    try:
        user_id = str(uuid.uuid4())
        password_hash = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
        new_user = User(id=user_id, name=user_name, password_hash=password_hash)
        sess.add(new_user)
        sess.commit()
        LOGGER.info('新建用户%s成功', user_id)
        return new_user
    except Exception as ex:
        LOGGER.error('注册用户异常', ex)
    finally:
        sess.close()


def signin(user_name, password):
    """用户登入"""
    pass
