# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_ddt_demo.py
@Description    :  
@CreateTime     :  2023/4/18 13:12
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/18 13:12
"""

import weeeTest
from weeeTest import log, testdata
import pytest


class TestDataDemo(weeeTest.TestCase):

    @weeeTest.params.data([
        ("First", "weeeTest"),
        ("Second", "sayweeeTest"),
        ("Third", "pytest_ddt"),
    ])
    def test_tuple_data(self, b, c):
        """
        方法参数化测试
        :param b:
        :param c:
        :return:
        """
        log.info("Testing: %s" % b)
        log.info("Testing: %s" % c)

    @weeeTest.params.data([
        ["First", "weeeTest"],
        ["Second", "sayweeeTest"],
        ["Third", "pytest_ddt"],
    ])
    def test_list_data(self, b, c):
        """
        方法参数化测试
        :param b:
        :param c:
        :return:
        """
        log.info("Testing: %s" % b)
        log.info("Testing: %s" % c)

    @weeeTest.params.data([
        {"First", "weeeTest"},
        {"Second", "sayweeeTest"},
        {"Third", "pytest_ddt"},
    ])
    def test_dict_data(self, b, c):
        """
        方法参数化测试
        :param b:
        :param c:
        :return:
        """
        log.info("Testing: %s" % b)
        log.info("Testing: %s" % c)


def data_mock():
    """
    mock参数化测试
    :return:
    """
    login_data = []
    for i in range(1, 5):
        login_data.append({
            "scene": f"login{i}",
            "username": testdata.get_email(),
            "password": testdata.get_int(100000, 999999)
        })
    return login_data


class TestMockDemo(weeeTest.TestCase):

    @weeeTest.params.data(data_mock())
    def test_login(self, _, username, password):
        """test login"""
        log.info(f"test username: {username}")
        log.info(f"test password: {password}")


if __name__ == '__main__':
    pytest.main()
