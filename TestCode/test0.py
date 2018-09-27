# coding:utf-8
__author__ = 'YangJun'

import logging


class Logger():
    def __init__(self, path, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.NOTSET)
        # 初始化控制台输出
        self.ch = logging.FileHandler
