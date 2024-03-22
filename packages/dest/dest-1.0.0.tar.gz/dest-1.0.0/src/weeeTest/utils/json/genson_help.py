# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  genson_help.py
@Description    :  
@CreateTime     :  2023/4/27 18:45
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/27 18:45
"""
import json

from genson import SchemaBuilder

from weeeTest.testdata.common.request import ResponseResult


def genson(data: dict = None):
    """
    return schema data
    """
    if (data is None) and ResponseResult.response is not None:
        data = ResponseResult.response

    builder = SchemaBuilder()
    builder.add_object(data)
    to_schema = json.dumps(builder.to_schema())
    return to_schema
