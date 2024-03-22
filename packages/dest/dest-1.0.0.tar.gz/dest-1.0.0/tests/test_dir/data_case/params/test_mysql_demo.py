# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_mysql_demo.py
@Description    :  
@CreateTime     :  2023/4/20 09:49
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/20 09:49
"""
import pytest

import weeeTest

from weeeTest import log


class TestMysqlDemo:
    @weeeTest.params.mysql(sql='select username,email from weee.user limit 2')
    def test_mysql_demo(self, username, email):
        """
        mysql查询结构参数化测试
        """
        # 注意：方法中的变量数量需要与sql查询结果的列数一致
        log.info("Testing userId :%s" % username)
        log.info("Testing username :%s" % email)


if __name__ == '__main__':
    pytest.main()
