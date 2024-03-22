# !/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

import pytest

import weeeTest

if __name__ == '__main__':
    # pytest.main(
    #     base_url="https://papi.tb1.sayweee.net",
    #     data_api_url="https://papi.tb1.sayweee.net",
    #     # case_list=["test_dir/api_case/test_api_request_demo.py"],
    #     debug=True,
    #     title="weeeTest 自带 Demo",
    #     tester="yingqing.shan",
    #     description="weeeTest 自带 Demo",
    #     language="zh-CN",
    #     rerun=0,
    #     weixin_access_token='92ed88af-6f5c-4d7c-be63-b23c1767e246',
    #     email_to='jialing.chen,yingqing.shan',
    #     email_to_dev="jialing.chen",
    #     ext=["-m", "api"]
    # )

    pytest.main(['-vs'])
