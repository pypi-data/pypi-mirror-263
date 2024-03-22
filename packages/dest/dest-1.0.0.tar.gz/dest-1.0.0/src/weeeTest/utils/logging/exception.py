# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  exception.py
@Description    :  
@CreateTime     :  2023/3/31 11:10
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/31 11:10
"""


class weeeTestException(Exception):
    """
    weeeTest exception
    """

    def __init__(self, msg, stacktrace: str = None):
        self.msg = msg
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = f"Message: {self.msg}\n"

        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += f"Stacktrace: {stacktrace}"
        return exception_msg


class weeeTestConfigException(weeeTestException):
    """
    weeeTest config exception
    """
    pass


class NotFindError(weeeTestException):
    """
    weeeTest config exception
    """
    pass


class TestFixtureRunError(weeeTestException):
    """
    weeeTest config exception
    """
    pass


class FileTypeError(weeeTestException):
    """
    weeeTest config exception
    """
    pass
