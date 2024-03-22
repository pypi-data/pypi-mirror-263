# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_redis_demo.py
@Description    :  
@CreateTime     :  2023/4/20 15:37
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/20 15:37
"""
import weeeTest

from weeeTest.utils import log
import pytest


class TestRedisDemo:
    @weeeTest.params.redis(key='myLock')
    def test_redis_demo(self, value):
        """
        读取redis-str参数化
        """
        log.info(f"读取redis-str参数化：{value}")


if __name__ == '__main__':
    pytest.main()
