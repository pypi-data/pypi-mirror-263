# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_api_depend_demo.py
@Description    :  
@CreateTime     :  2023/5/8 15:15
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/5/8 15:15
"""
import pytest

import weeeTest


class TestDependDemo(weeeTest.TestCase):

    def test_dependencies(self):
        """
        测试依赖
        """
        self.post('/api/v1/auth/login', json={'username': 'admin', 'password': 'password@123'})
        token = self.response['data']['token']

        self.get('/api/v1/user/list', params="username=testuser", headers={'Authorization': 'Bearer ' + token})
        self.assert_status_code(200)
        assert self.response['code'] == 20000


if __name__ == '__main__':
    pytest.main()
