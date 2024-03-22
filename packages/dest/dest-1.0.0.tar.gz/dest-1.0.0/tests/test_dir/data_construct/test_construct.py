# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  test_construct.py
@Description    :  
@CreateTime     :  2023/5/9 13:22
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/5/9 13:22
"""

import weeeTest
from weeeTest import testdata
import pytest


class TestConstruct(weeeTest.TestCase):

    def test_get_first_name(self):
        # 随机一个名
        print("名字：", testdata.first_name())
        print("名字(男)：", testdata.first_name(gender="male"))
        print("名字(女)：", testdata.first_name(gender="female"))
        print("名字(中文男)：", testdata.first_name(gender="male", language="zh"))
        print("名字(中文女)：", testdata.first_name(gender="female", language="zh"))

    def test_get_last_name(self):
        # 随机一个姓
        print("姓:", testdata.last_name())
        print("姓(中文):", testdata.last_name(language="zh"))

    def test_get_full_name(self):
        # 随机一个全名
        print("姓名:", testdata.username())
        print("姓名(中文):", testdata.username(language="zh"))

    def test_get_address(self):
        # 随机一个地址
        print("地址:", testdata.address())
        print("地址(中文):", testdata.address(language="zh"))

    def test_get_birthday(self):
        # 随机一个生日
        print("生日:", testdata.get_birthday())
        print("生日字符串:", testdata.get_birthday(as_str=True))
        print("生日年龄范围:", testdata.get_birthday(start_age=20, stop_age=30))

    def test_get_date(self):
        # 随机一个日期
        print("日期:", testdata.get_date())
        print("日期(昨天):", testdata.get_date(-1))
        print("日期(明天):", testdata.get_date(1))

        print("当月：", testdata.get_month())
        print("上个月：", testdata.get_month(-1))
        print("下个月：", testdata.get_month(1))

        print("今年：", testdata.get_year())
        print("去年：", testdata.get_year(-1))
        print("明年：", testdata.get_year(1))

        print("当周：", testdata.get_week())
        print("上周：", testdata.get_week(-1))
        print("下周：", testdata.get_week(1))

    def test_get_digits(self):
        # 随机一个数字
        print("数字(8位):", testdata.get_digits(8))

    def test_get_phone(self):
        # 随机一个电话
        print("手机号:", testdata.get_phone())
        print("手机号(移动):", testdata.get_phone(operator="mobile"))
        print("手机号(联通):", testdata.get_phone(operator="unicom"))
        print("手机号(电信):", testdata.get_phone(operator="telecom"))

    def test_get_email(self):
        # 随机一个邮箱
        print("邮箱:", testdata.get_email())
        print("邮箱(163):", testdata.get_email(domain="163.com"))

    def test_get_float(self):
        # 随机一个浮点数
        print("浮点数:", testdata.get_float())
        print("浮点数范围:", testdata.get_float(min_size=1.0, max_size=2.0))

    def test_get_datatime(self):
        # 随机一个时间
        print("当前时间:", testdata.get_now_datetime())
        print("当前时间(格式化字符串):", testdata.get_now_datetime(strftime=True))
        print("未来时间:", testdata.get_future_datetime())
        print("未来时间(格式化字符串):", testdata.get_future_datetime(strftime=True))
        print("过去时间:", testdata.get_past_datetime())
        print("过去时间(格式化字符串):", testdata.get_past_datetime(strftime=True))

    def test_get_other(self):
        # 随机数据
        print("整型:", testdata.get_int())
        print("整型32位:", testdata.get_int32())
        print("整型64位:", testdata.get_int64())
        print("MD5:", testdata.get_md5())
        print("UUID:", testdata.get_uuid())

    def test_get_words(self):
        # 随机单词
        print("单词:", testdata.get_word())
        print("单词组(3个):", testdata.get_words(3))


if __name__ == '__main__':
    pytest.main()
