# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  coversion.py
@Description    :  
@CreateTime     :  2023/4/18 13:10
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/18 13:10
"""


def check_data(list_data: list) -> list:
    """
    Checking test data format.
    :param list_data:
    :return:
    """
    if isinstance(list_data, list) is False:
        raise TypeError("The data format is not `list`.")
    if len(list_data) == 0:
        raise ValueError("The data format cannot be `[]`.")
    if isinstance(list_data[0], dict):
        test_data = []
        for data in list_data:
            line = []
            for d in data.values():
                line.append(d)
            test_data.append(line)
        return test_data

    return list_data
