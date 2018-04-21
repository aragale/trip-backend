import datetime
import json

from sqlalchemy import TypeDecorator, types, Column, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

# 基类
BASE = declarative_base()


class Json(TypeDecorator):
    """类型装饰类"""

    @property
    def python_type(self):
        return object

    impl = types.String

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
    user_id = Column(String(36), ForeignKey('users.id'))
    time = Column(DateTime, default=datetime.datetime.now())


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
    time = Column(DateTime, default=datetime.datetime.now(), comment='时间')
    description = Column(Text, comment='文字描述')
    images = Column(Json, comment='照片url列表')
    trace_id = Column(String(36), ForeignKey('traces.id'))


class Trace(BASE):
    """路途"""
    __tablename__ = 'traces'
    id = Column(String(36), primary_key=True)
    positions = Column(Json, comment='定位点列表')
