import logging
import uuid

from flask_restful import abort
from sqlalchemy import func

from ..data import get_session
from ..models import Session, User
from ..service import user

LOGGER = logging.getLogger(__name__)


def is_valid(id):
    """检查会话是否有效"""
    if id is None:
        return False
    else:
        sess = get_session()
        try:
            return sess.query(func.count(Session.id)). \
                       filter_by(id=id, is_deleted=0). \
                       limit(1). \
                       scalar() != 0
        except Exception as ex:
            LOGGER.error('验证会话异常', ex)
        finally:
            sess.close()


def exists_by_user_name(user_name):
    """根据用户名查询是否存在会话"""
    sess = get_session()
    try:
        count = sess.query(func.count(Session.id)). \
            join(User). \
            filter(User.name == user_name). \
            limit(1). \
            scalar()
        return count != 0
    except Exception as ex:
        LOGGER.error('根据用户姓名查询会话异常', ex)
    finally:
        sess.close()


def sign_in(user_name, password):
    """登入"""
    if user_name is None or password is None:
        abort(400, error='信息不正确')
    sess = get_session()
    try:
        if user.check_password(user_name, password):
            user_id = user.get_id_by_name(user_name)
            # 删除原有效会话
            sess.query(Session). \
                filter_by(user_id=user_id). \
                delete(synchronize_session=False)
            # 创建新的会话
            session_id = str(uuid.uuid4())
            new_session = Session(id=session_id, user_id=user_id)
            sess.add(new_session)
            # 提交会话
            sess.commit()
            LOGGER.info('用户"%s"登入"%s"', user_name, session_id)
            return {'user_id': user_id, 'session': session_id}
    except Exception as ex:
        LOGGER.error('登入异常', ex)
    finally:
        sess.close()


def sign_out(session_id):
    """登出"""
    sess = get_session()
    try:
        ret = sess.query(Session). \
            filter_by(id=session_id). \
            delete(synchronize_session=False)
        sess.commit()
        return ret
    except Exception as ex:
        LOGGER.error('登出异常', ex)
    finally:
        sess.close()


def get_user_id_by_id(session_id):
    """根据会话ID查询用户ID"""
    sess = get_session()
    try:
        return sess.query(Session.user_id). \
            filter_by(id=session_id). \
            limit(1). \
            scalar()
    except Exception as ex:
        LOGGER.error('根据会话ID查询用户ID异常', ex)
    finally:
        sess.close()
