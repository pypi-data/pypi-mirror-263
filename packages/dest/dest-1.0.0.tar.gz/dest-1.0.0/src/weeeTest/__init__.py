# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  __init__.py
@Description    :  
@CreateTime     :  2023/3/22 12:18
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/22 12:18
"""
from .case import TestCase
from .config import Message
from .config import RunResult
from .config import weeeConfig
from .data_process import data
from .mark import mark
from .parameters import params
from .testdata.common.request.RequestUtil import HttpRequest
from .testdata.common.request.RequestUtil import ResponseCheck
from .testdata.common.structure import random_fun as testdata
from .utils.cache import cache
from .utils.check import check
from .utils.file import file
from .utils.json.genson_help import genson
from .utils.json.jmespath_help import jmespath
from .utils.logging import log, log_cfg
from .utils.push import EmailSMTP as emailSMTP, Weinxin as weinXin
from .version import version, get_version

__all__ = ["TestCase", "data", "params", "mark", "cache", "file", "jmespath", "log", "log_cfg", "emailSMTP",
           "check", "weinXin", "get_version", "version", "ResponseCheck", "genson", "testdata", "HttpRequest",
           "Message", "RunResult"]

__author__ = "yingqing.shan"
# 版本说明
# --------------------
"""
0.0.0.0
版本说明：
第一位：大版本号，新需求或者重大变更
第二位：小版本号，新功能或者新特性
第三位：修订号，bug修复
第四位：编译号，内部编译号或本地测试版本号
"""

""" 
版本号后缀说明：
a1：Alpha 版本
b1：Beta 版本
rc1：Release Candidate 版本
"""
__version__ = "1.0.0"
