""" 足迹逻辑 """
import logging
import uuid

from ..data import get_session
from ..models import FootPrint

LOGGER = logging.getLogger(__name__)


def create(json, user_id):
    """ 创建足迹 """
    title = json.get('title')
    description = json.get('description')
    images = json.get('images')
    trace_id = json.get('trace_id')
    # 实例化新的足迹
    new_foot_print = FootPrint(
        id=str(uuid.uuid4()),
        title=title,
        user_id=user_id,
        description=description,
        images=images,
        trace_id=trace_id)
    sess = get_session()
    try:
        sess.add(new_foot_print)
        sess.commit()
        return new_foot_print
    except Exception as ex:
        LOGGER.error('创建足迹异常')
        return None
    finally:
        sess.close()
