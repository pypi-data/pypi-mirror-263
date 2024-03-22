# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :   report.py
@Description    :
@CreateTime     :  2023/3/22 12:18
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/22 12:18
"""
import ast
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INIT_FILE = os.path.join(BASE_DIR, "__init__.py")


# ---------------------------
# Read version number
# ---------------------------
def get_version():
    _version_re = re.compile(r'__version__\s+=\s+(.*)')
    with open(INIT_FILE, 'rb') as f:
        _version = str(ast.literal_eval(_version_re.search(
            f.read().decode('utf-8')).group(1)))

    return _version


get_version = get_version()
# 获取版本号
version = get_version
