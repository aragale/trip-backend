"""用户逻辑模块"""
import hashlib
import logging
import uuid

from flask_restful import abort
from sqlalchemy import func

from ..data import get_session
from ..models import User
from ..service import session

LOGGER = logging.getLogger(__name__)


def sign_up(user_name, password):
    """用户注册"""
    if user_name is None or password is None:
        # 信息不完整
        abort(400, error='Incomplete parameters')
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


def get_id_by_name(name):
    sess = get_session()
    try:
        return sess.query(User.id).filter_by(name=name).limit(1).scalar()
    except Exception as ex:
        LOGGER.error('查询是否存在指定用户名用户异常', ex)
        raise ex
    finally:
        sess.close()


def exists_by_id(id):
    sess = get_session()
    try:
        return sess.query(func.count(User.id)).filter_by(id=id).scalar() != 0
    except Exception as ex:
        LOGGER.error('查询是否存在指定ID用户异常', ex)
        raise ex
    finally:
        sess.close()


def delete(id, session_id):
    """删除用户"""
    if not session.is_valid(session_id):
        abort(403, error='无权限，请登录')
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
            one()
        return selected
    except Exception as ex:
        LOGGER.error('检查密码异常', ex)
    finally:
        sess.close()
