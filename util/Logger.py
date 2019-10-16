#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 22:10
# @Author  : Weiqiang.long
# @Site    : 
# @File    : Logger.py
# @Software: PyCharm

"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'log')
        self.log_file_name = 'mock-service.log'  # 日志文件
        self.backup_count = 30  # 保留的日志数量
        # 日志输出级别
        self.console_output_level = 'INFO'
        self.file_output_level = 'INFO'
        # 日志输出格式
        pattern = '%(asctime)s - %(filename)s [Line:%(lineno)d] - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。
        """
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            # 每天生成的日志文件没有后缀，需要修改源码：TimedRotatingFileHandler类下的doRollover方法-->
            # dfn = self.rotation_filename(self.baseFilename + "." + time.strftime(self.suffix, timeTuple)后面拼接后缀名
            # dfn = self.rotation_filename(self.baseFilename + "." + time.strftime(self.suffix, timeTuple) + ".log")
            file_handler = TimedRotatingFileHandler(filename=os.path.join(self.log_path, self.log_file_name),
                                                    when='MIDNIGHT',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()