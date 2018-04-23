"""用户逻辑模块"""
import hashlib
import logging
import uuid

from ..data import get_session
from ..models import User
from ..service import session

LOGGER = logging.getLogger(__name__)


def sign_up(user_name, password):
    """用户注册"""
    if user_name is None or password is None:
        # 信息不完整
        return {}
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
        # 返回空
        return {}
    finally:
        sess.close()


def delete(id, session_id):
    """删除用户"""
    if not session.is_valid(session_id):
        return {}
    sess = get_session()
    try:
        ret = sess.query(User). \
            filter_by(id=id). \
            delete(synchronize_session=False)
        sess.commit()
        return 'ok' if ret == 0 else 'not exists'
    except Exception as ex:
        LOGGER.error('禁用用户异常', ex)
        raise ex
    finally:
        sess.close()


def get_by_name_and_password(user_name, password):
    """根据用户名和密码查询用户"""
    sess = get_session()
    try:
        selected = sess.query(User). \
            filter_by(name=user_name, password_hash=hashlib.sha3_512(password.encode('utf-8')).hexdigest()). \
            limit(1). \
            first()
        return selected
    except Exception as ex:
        LOGGER.error('检查密码异常', ex)
    finally:
        sess.close()
