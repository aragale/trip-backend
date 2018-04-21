"""数据库"""
import logging
import logging.config

import os.path
import yaml


def setup_logging():
    """
    配置日志
    """
    os.makedirs('../logs')
    path = 'logging.yaml'
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)


LOGGER = logging.getLogger(__name__)
