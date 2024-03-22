# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  common.py
@Description    :  
@CreateTime     :  2023/5/8 17:24
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/5/8 17:24
"""
import weeeTest
from weeeTest import HttpRequest


class Common(HttpRequest):

    @weeeTest.ResponseCheck.response(describe="获取登录用户名", status_code=200, jmespath_search="headers.Account",
                                     check={"headers.Host": "httpbin.org"}, debug=True)
    def get_login_user(self):
        """
        调用接口获得用户名
        断言：
        返回状态码为200，
        返回值中headers.Account的值为bugmaster，
        返回值中headers.Host的值为httpbin.org，

        * `describe` : 封装方法描述。
        * `status_code`: 判断接口返回的 HTTP 状态码，默认`200`。
        * `ret`: 提取接口返回的字段，参考`jmespath` 提取规则。
        * `ResponseCheck`: 检查接口返回的字段。参考`jmespath` 提取规则。
        * `debug`: 开启`debug`，打印更多信息。

        """
        headers = {"Account": "bugmaster"}
        r = self.get("http://httpbin.org/get", headers=headers)
        # 断言需要把 返回值交给装饰器处理
        return r


if __name__ == '__main__':
    c = Common()
    c.get_login_user()
