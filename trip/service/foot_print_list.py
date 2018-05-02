""" 足迹列表逻辑 """
import logging
from ..data import get_session
from ..models import FootPrint

LOGGER = logging.getLogger(__name__)


def get(user_id):
    """获取足迹列表"""
    sess = get_session()
    try:
        result = sess.query(FootPrint.id).\
            filter_by(user_id=user_id).\
            all()
            # 解开元祖，生成字符串列表
        return list(r[0] for r in result)
    except Exception as ex:
        LOGGER.error('获取足迹列表', ex)
        return None
    finally:
        sess.close()
