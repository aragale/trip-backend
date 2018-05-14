""" 足迹列表逻辑 """
import logging
from ..data import get_session
from ..models import FootPrint

LOGGER = logging.getLogger(__name__)


def get(user_id):
    """获取足迹列表"""
    sess = get_session()
    try:
        return sess.query(FootPrint).\
            filter_by(user_id=user_id).\
            order_by(FootPrint.time.desc()).\
            all()
    except Exception as ex:
        LOGGER.error('获取足迹列表', ex)
        return []
    finally:
        sess.close()
