# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_file_demo.py
@Description    :  
@CreateTime     :  2023/4/21 09:54
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/21 09:54
"""
import weeeTest
from weeeTest import log
import pytest


class TestFileDem:
    @weeeTest.params.file(file_name='csv_data.csv')
    def test_file_csv_demo(self, username, password):
        """
        测试 csv 文件
        """
        log.info(' username = %s, password = %s' % (username, password))

    @weeeTest.params.file(file_name='excel_data.xlsx')
    def test_file_xlsx_demo(self, username, password):
        """
        测试 xlsx 文件
        """
        log.info(' username = %s, password = %s' % (username, password))

    @weeeTest.params.file(file_name='json_data.json', key='login1')
    def test_file_json_demo(self, username, password):
        """
        测试 json 文件
        """
        log.info(' username = %s, password = %s' % (username, password))

    @weeeTest.params.file(file_name='yaml_data.yaml', key='login1')
    def test_file_yaml_demo(self, username, password):
        """
        测试 yaml 文件
        """
        log.info(' username = %s, password = %s' % (username, password))


if __name__ == '__main__':
    pytest.main()
