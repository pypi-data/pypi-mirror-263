# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Jialing chen
@Version        :  V1.0.0
------------------------------------
@File           :  test_mysql_demo.py
@Description    :  
@CreateTime     :  2023/4/19 17:56
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/19 17:56
"""
import pytest

import weeeTest
from weeeTest.utils.logging import log


class TestMysqlDemo:

    @weeeTest.data.mysql(sql='select userId,username from weee.user limit 2')
    def test_select_ec(self, *args):
        log.info(f'从数据库中获取查询结果::{args[0]}')

    @weeeTest.data.mysql(
        sql="insert student(name,age,sum)value('testhhh',10,200)",
        host='localhost', user='root', password='123456', port='3306', db='test_db')
    def test_update(self, *args):
        log.info(f'成功执行数据库,影响行数::{args[0]}')


if __name__ == '__main__':
    pytest.main()
