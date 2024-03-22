# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Jialing chen
@Version        :  V1.0.0
------------------------------------
@File           :  test_redis_demo.py
@Description    :  
@CreateTime     :  2023/4/20 18:13
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/20 18:13
"""
import pytest

import weeeTest
from weeeTest.utils.logging import log


class TestRedisDemo:

    @weeeTest.data.redis(key='test_str', redis_conn_env='dev')
    def test_read_str(self, *args):
        log.info(f'读取的redis值-str::{args[0]}')

    @weeeTest.data.redis(key='test_list', redis_conn_env='dev')
    def test_read_list(self, *args):
        log.info(f'读取的redis值-list::{args[0]}')

    @weeeTest.data.redis(key='test_write_str', value='test_write_str_value', redis_conn_env='dev')
    def test_write_str(self, *args):
        log.info(f'写入的redis值-str::{args[0]}')

    @weeeTest.data.redis(key='test_write_list', value=['first', 'second', 'third'], redis_conn_env='dev')
    def test_write_list(self, *args):
        log.info(f'写入的redis值-list{args[0]}')


if __name__ == '__main__':
    pytest.main()
