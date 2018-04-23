"""会话逻辑"""
import logging
import uuid

from sqlalchemy import func

from ..data import get_session
from ..models import Session
from ..service import user

LOGGER = logging.getLogger(__name__)


def get(session_id):
    """根据ID获取会话"""
    if session_id is None:
        return {}
    else:
        sess = get_session()
        try:
            return sess.query(Session). \
                filter_by(id=session_id). \
                limit(1). \
                first()
        except Exception as ex:
            LOGGER.error('根据ID获取会话异常', ex)
        finally:
            sess.close()


def is_valid(session_id):
    """检查会话是否有效"""
    if session_id is None:
        return False
    else:
        sess = get_session()
        try:
            return sess.query(func.count(Session.id)). \
                       filter_by(id=session_id). \
                       limit(1). \
                       scalar() != 0
        except Exception as ex:
            LOGGER.error('验证会话异常', ex)
        finally:
            sess.close()


def sign_in(user_name, password):
    """登入"""
    if user_name is None or password is None:
        # 返回空
        return {}
    sess = get_session()
    try:
        # 查询对应的用户
        selected_user = user.get_by_name_and_password(user_name, password)
        # 判断查询到的用户
        if selected_user:
            # 若用户存在
            user_id = selected_user.id
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
        else:
            # 若用户不存在
            return {}
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
        LOGGER.info('会话%s登出', session_id)
        sess.commit()
        return {'status': 'ok'} if ret == 1 else {}
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
