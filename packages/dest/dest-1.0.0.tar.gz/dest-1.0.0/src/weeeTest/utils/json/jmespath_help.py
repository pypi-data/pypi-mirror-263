# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  jmespath_help.py
@Description    :  
@CreateTime     :  2023/3/30 11:37
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/30 11:37
"""
from jmespath import search


def jmespath(data, expression, options=None):
    """
    search jmespath data
    jmespath search data
    https://github.com/jmespath/jmespath.py
    """
    return search(expression, data, options)
