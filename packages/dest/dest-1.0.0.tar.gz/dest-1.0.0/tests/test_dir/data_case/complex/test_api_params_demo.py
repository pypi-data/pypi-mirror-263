# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_api_params_demo.py
@Description    :  
@CreateTime     :  2023/4/25 09:54
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/25 09:54
"""
import pytest

import weeeTest
from weeeTest import log


class TestAPIParamsDemo(weeeTest.TestCase):
    @pytest.fixture(scope='class')
    def login(self):
        """
        登录获取token
        """

        self.post('/api/v1/auth/login', json={'username': 'admin', 'password': 'password@123'})
        return self.response['data']['token']

    @weeeTest.params.data([
        ("First", "weeeTest"),
        ("Second", "sayweeeTest"),
        ("Third", "pytest_ddt"),
        ("Fourth", "py_ddt")
    ], "a,b")
    def test_data_demo(self, login, a, b):
        """
        方法参数化测试
        :param a:
        :param b:
        :return:
        """
        self.get('/api/v1/user/list', params="username=testuser", headers={'Authorization': 'Bearer ' + login})
        self.assert_status_code(200)
        assert self.response['code'] == 20000
        log.info("Testing: %s" % b)
        log.info("Testing: %s" % a)


if __name__ == '__main__':
    pytest.main(base_url="https://papi.tb1.sayweee.net")
