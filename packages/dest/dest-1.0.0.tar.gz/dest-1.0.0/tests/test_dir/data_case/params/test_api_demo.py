# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_api_demo.py
@Description    :  
@CreateTime     :  2023/4/19 10:28
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/19 10:28
"""
import pytest

import weeeTest
from weeeTest import log


class TestApiDemo(weeeTest.TestCase):

    @weeeTest.params.data_api(url="/api/v1/user/list?pageSize=10&current=1", ret="data")
    def test_api_demo(self, id, username, email, nickname, fullname, role, source, avatar, is_valid, phone, sex, status,
                      desc, created_at, updated_at, is_deleted, update_user, last_login_at, client_host):
        """
         需要注意参数化的值需要会返回的数组里的值数量一致
        """
        log.info(f"id: {id}, username:{username}, email: {email} ")


if __name__ == '__main__':
    pytest.main()
