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

import weeeTest
from weeeTest.utils.logging import log
import pytest


class TestFileDemo:

    @weeeTest.data.file(file_name='excel_data.xlsx')
    def test_read_xls(self, *args):
        log.info(f'读取的xls值:::{args[0]}')

    @weeeTest.data.file(file_name='csv_data.csv')
    def test_read_csv(self, *args):
        log.info(f'读取的csv值{args[0]}')

    @weeeTest.data.file(file_name='json_data.json')
    def test_read_json(self, *args):
        log.info(f'读取的json值{args[0]}')

    @weeeTest.data.file(file_name='testData.yaml', return_type='dict')
    def test_read_yaml(self, *args):
        log.info(f'读取的yaml值{args[0]}')


if __name__ == '__main__':
    pytest.main()
