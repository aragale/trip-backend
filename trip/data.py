"""数据库模块"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

from .models import BASE as __BASE

__ENGINE = create_engine('sqlite:///trip.db', echo=True)
# 若不存在表，则创建表
__BASE.metadata.create_all(__ENGINE)
__SESSION_MAKER: sessionmaker = sessionmaker(bind=__ENGINE, expire_on_commit=False)


def get_session() -> session:
    """获取数据库会话"""
    return __SESSION_MAKER()
