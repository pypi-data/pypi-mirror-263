# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  check_log.py
@Description    :  
@CreateTime     :  2023/5/31 11:20
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/5/31 11:20
"""
from weeeTest.utils.logging import log


def log_failure(msg="", check_str=""):
    msg = str(msg).strip()

    if check_str:
        msg = f"FAILURE: {msg}: {check_str}"
    log.error(f"[ {msg} ]")
