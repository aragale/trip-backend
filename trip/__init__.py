import os

from .config import setup_logging

# 创建日志文件夹
os.makedirs('../logs', exist_ok=True)
# 配置日志
setup_logging()
