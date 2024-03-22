# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_class_demo.py
@Description    :  
@CreateTime     :  2023/4/18 18:04
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/18 18:04
"""
import weeeTest
from weeeTest import log
import pytest


@weeeTest.params.data_class(("key", "value"), [("weeeTest", "https://www.sayweee.com"), ("name", "weeeTest")])
class TestClassDemo(weeeTest.TestCase):
    """
    类参数化测试
    """

    def test_data_class_demo(self):
        """
         类参数化测试
        """
        log.info("Testing key :%s" % self.key)
        log.info("Testing value :%s" % self.value)


if __name__ == '__main__':
    pytest.main()
