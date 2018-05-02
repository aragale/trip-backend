""" 足迹逻辑 """
import logging
import uuid

from ..data import get_session
from ..models import FootPrint, Trace

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
        LOGGER.error('创建足迹异常', ex)
        return None
    finally:
        sess.close()


def get(foot_print_id):
    """ 获取足迹 """
    sess = get_session()
    try:
        return sess.query(FootPrint). \
            filter_by(id=foot_print_id). \
            first()
    except Exception as ex:
        LOGGER.error('获取足迹异常', ex)
        return None
    finally:
        sess.close()


def update(foot_print_id, json):
    """ 修改足迹 """
    sess = get_session()
    # 由foot_print_id查出原有足迹
    source = sess.query(FootPrint).\
        filter_by(id=foot_print_id). \
        first()
    if source is None:
        return None
    else:
        try:
            source.title = json.get('title')
            source.images = json.get('images')
            source.trace_id = json.get('trace_id')
            source.description = json.get('description')
            # 提交
            sess.commit()
            return source
        except Exception as ex:
            LOGGER.error('修改足迹异常', ex)
            return None
        finally:
            sess.close()


def delete(foot_print_id):
    """ 删除足迹 """
    sess = get_session()
    try:
        # 查询足迹
        old_foot_print_list = sess.query(FootPrint).\
            filter_by(id=foot_print_id).\
            all()
        # delete(synchronize_session=False)
        if old_foot_print_list:
            # 删除对应的路途
            sess.query(Trace).\
                filter_by(id=old_foot_print_list[0].trace_id).\
                delete(synchronize_session=False)
            # 删除足迹
            sess.delete(old_foot_print_list[0])
        sess.commit()
        return ''
    except Exception as ex:
        LOGGER.error('删除足迹', ex)
        return ''
    finally:
        sess.close()
