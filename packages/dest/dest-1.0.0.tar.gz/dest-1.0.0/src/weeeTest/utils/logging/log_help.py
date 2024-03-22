# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  log.py
@Description    :  
@CreateTime     :  2023/3/23 18:14
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/23 18:14
"""
import inspect
import os
import sys
import time

from loguru import logger

from weeeTest.config import weeeConfig

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
exec_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(exec_dir, "reports")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
now_date = time.strftime("%Y_%m_%d")
if weeeConfig.log_path is None:
    weeeConfig.log_path = os.path.join(report_dir, now_date + ".log")
if weeeConfig.report_path is None:
    weeeConfig.report_path = os.path.join(report_dir, now_time + "_result.html")

# 文件日志格式
file_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>文件路径: {file.path}</cyan> | <cyan>执行路径: {name}::{function}::{line}</cyan> | <level>msg: {message}</level>"

# 终端日志格式
terminal_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>执行路径: {name}::{function}::{line}</cyan> | <level>msg: {message}</level>"


class LogConfig:
    """log config"""

    def __init__(self, level: str = "DEBUG", colorlog: bool = True):
        self.logger = logger
        self._colorlog = colorlog
        self._console_format = terminal_FORMAT
        self._log_format = file_FORMAT
        self._level = level
        self.logfile = weeeConfig.log_path
        self.set_level(self._colorlog, self._console_format, self._level)

    def set_level(self, colorlog: bool = True, format: str = None, level: str = "DEBUG"):
        """
        setting level
        :param colorlog:
        :param format:
        :param level:
        :return:
        """
        if format is None:
            format = self._console_format
        self.logger.remove()
        self._level = level
        self.logger.add(sys.stderr, level=level, colorize=colorlog, format=format)
        self.logger.add(self.logfile, level=level, colorize=False, format=self._log_format, encoding="utf-8")


# log level: TRACE < DEBUG < INFO < SUCCESS < WARNING < ERROR
log_cfg = LogConfig(level="TRACE")
log = logger
