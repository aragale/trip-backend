"""配置模块"""
import logging
import logging.config

import os.path
import yaml

LOGGER = logging.getLogger(__name__)
# 切换工作路径到本文件所在路径
path_of_file = os.path.dirname(os.path.abspath(__file__))
os.chdir(path_of_file)
LOGGER.info('Changed the current working directory to %s', path_of_file)


def setup_logging():
    """配置日志"""
    logging_config_path = './logging.yaml'
    if os.path.exists(logging_config_path):
        with open(logging_config_path, 'rt') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
