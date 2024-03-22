# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_api_common_depend_demo.py
@Description    :  
@CreateTime     :  2023/5/8 17:22
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/5/8 17:22
"""
import pytest

import weeeTest
from .common import Common


class TestApiResponseDependDemo(weeeTest.TestCase):
    def setup_class(self):
        self.c = Common()

    @weeeTest.mark.list('api')
    def test_api_response_depend_demo(self):
        """
        测试接口返回值依赖
        """
        # 调用 get_login_user() 获取
        user = self.c.get_login_user()
        self.post("http://httpbin.org/post", data={'username': user})
        self.assert_status_code(200)


if __name__ == '__main__':
    pytest.main()
