"""模型类模块"""
import datetime
import json
from collections import namedtuple

from sqlalchemy import TypeDecorator, types, Column, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

# 基类
BASE = declarative_base()


class Json(TypeDecorator):
    """类型装饰类"""

    @property
    def python_type(self):
        return object

    impl = types.Text

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_literal_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        try:
            return json.loads(value)
        except (ValueError, TypeError):
            return None


class Session(BASE):
    """会话"""
    __tablename__ = 'sessions'
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey('users.id'), comment='用户id')
    time = Column(DateTime, default=datetime.datetime.now(), comment='创建时间')


class User(BASE):
    """用户"""
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True)
    name = Column(String(36), unique=True, comment='用户名称，不可重复')
    password_hash = Column(String(128), comment='密码的SHA512哈希值')


class FootPrint(BASE):
    """足迹"""
    __tablename__ = 'foot_prints'
    id = Column(String(36), primary_key=True)
    title = Column(String(100), comment='标题')
    user_id = Column(String(36), ForeignKey('users.id'), comment='用户ID')
    time = Column(DateTime, default=datetime.datetime.now(), comment='时间')
    description = Column(Text, comment='文字描述')
    images = Column(Json, comment='照片url列表')
    trace_id = Column(String(36), ForeignKey('traces.id'))


class Trace(BASE):
    """路途"""
    __tablename__ = 'traces'
    id = Column(String(36), primary_key=True)
    positions = Column(Json, comment='定位点列表')


# 定位点
Position = namedtuple('Position', 'time longitude latitude')


def __position_hook(dct):
    """定位对象钩子"""
    return namedtuple('Position', dct.keys())(*dct.values())


def as_position(json_string):
    """字符串转定位点对象"""
    return json.loads(json_string, object_hook=__position_hook)


def as_position_list(json_string):
    """字符串转定位点对象列表"""
    dcts = json.loads(json_string)
    return list(__position_hook(dct) for dct in dcts)


class FootPrintShare(BASE):
    """ 足迹分享表 """
    __tablename__ = 'foot_print_share'
    id = Column(String(36), primary_key=True)
    source_user_id = Column(String(36), ForeignKey('users.id'), comment='来源用户ID')
    target_user_id = Column(String(36), ForeignKey('users.id'), comment='目标用户ID')
    foot_print_id = Column(String(36), ForeignKey('foot_prints.id'), comment='足迹ID')
    time = Column(DateTime, default=datetime.datetime.now(), comment='分享时间')
