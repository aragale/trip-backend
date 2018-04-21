import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

# 基类
BASE = declarative_base()


class User(BASE):
    """用户"""
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    name = Column(String(36), unique=True, comment='用户名称，不可重复')
    password_hash = Column(String(128), comment='密码的SHA512哈希值')


class FootPrint(BASE):
    """足迹"""
    __tablename = 'foot_prints'

    id = Column(String(36), primary_key=True)
    title = Column(String(100), comment='标题')
    time = Column(DateTime, default=datetime.datetime.now(), comment='时间')
    description = Column(Text, comment='文字描述')
    images = Column(JSON, comment='照片url列表')
    trace_id = Column(String(36), ForeignKey('traces.id'))


class Trace(BASE):
    """路途"""
    __tablename__ = 'traces'

    id = Column(String(36), primary_key=True)
    positions = Column(JSON, comment='定位点列表')