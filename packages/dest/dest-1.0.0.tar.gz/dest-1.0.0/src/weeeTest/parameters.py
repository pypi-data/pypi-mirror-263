# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  param.py
@Description    :  
@CreateTime     :  2023/4/12 10:52
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/12 10:52
"""
import inspect
import warnings

from parameterized.parameterized import skip_on_empty_helper, parameterized_class, reapply_patches_if_need, \
    delete_patches_if_need

from weeeTest import mark
from weeeTest.config import weeeConfig
from weeeTest.testdata.base.parameterization import default_name_func, default_doc_func, parameterized
from weeeTest.testdata.common.file import FileData
from weeeTest.testdata.common.mysql import MysqlCommon
from weeeTest.testdata.common.redis import RedisCommon
from weeeTest.testdata.common.request import HttpRequest
from weeeTest.testdata.coversion import check_data
from weeeTest.utils.logging import log

__all__ = ['params']

from weeeTest.utils import jmespath


class Parameters:

    def mysql(self, sql: str):
        """
        mysql参数化
        :param sql:  sql语句
        :return:
        """
        return self.data(MysqlCommon.mysql_param(sql=sql))

    def redis(self, key: str):
        """
        redis参数化
        :param key:  redis的key
        :return:
        """
        return self.data(RedisCommon().redis_param(key=key))

    def file(self, file_name: str, sheet: str = "Sheet1", start_line: int = 1, end_line: int = None, key: str = None,
             test_data_dir_name: str = 'test_data'):
        """
        文件参数化
        :param file_name:  文件名称
        :param sheet:  sheet名称
        :param start_line:  起始行
        :param end_line:  结束行
        :param key: 提取接口返回的字段，参考`jmespath`的search提取规则。如：jmespath.search('foo.bar', {'foo': {'bar': 'baz'}})
        :param test_data_dir_name 测试数据文件夹名称
        :return:
        """
        return self.data(
            FileData().file_data_param(file_name=file_name, sheet=sheet, line=start_line, end_line=end_line,
                                       jmespath_search=key, test_data_dir_name=test_data_dir_name))

    @classmethod
    def data(cls, input_values, attrs=None, name_func=None, doc_func=None, skip_on_empty=False, **legacy):
        """
        参数化测试用例的“蛮力”方法。 创建新的测试用例并将它们注入到定义包装函数的命名空间中。对于“UnitTest”子类中的参数化测试很有用，其中 Nose 测试生成器不起作用。
        :param attrs: 这是字符串列表，它指定要复制到测试用例的属性。如果没有提供，则将复制所有属性。
        :param  input_values：要传递给测试函数的可迭代值
        :param name_func: 一个函数，它接受一个参数（输入可迭代的值）并返回一个字符串以用作测试用例的名称。如果没有提供，测试用例的名称将是测试函数的名称加上参数值。
        :param doc_func: 一个函数，它接受一个参数（输入可迭代的值）并返回一个字符串以用作测试用例的文档字符串。如果没有提供，测试用例的文档字符串将是测试函数的文档字符串。
        :param skip_on_empty: 如果为真，则如果输入可迭代对象为空，则将跳过测试。如果为 False，则在输入可迭代对象为空时将引发 ValueError
        """
        if attrs is not None:
            return mark.parametrize(attrs, input_values)
        input_values = check_data(input_values)
        if "testcase_func_name" in legacy:
            warnings.warn("testcase_func_name= is deprecated; use name_func=", DeprecationWarning, stacklevel=2)
            if not name_func:
                name_func = legacy["testcase_func_name"]

        if "testcase_func_doc" in legacy:
            warnings.warn("testcase_func_doc= is deprecated; use doc_func=", DeprecationWarning, stacklevel=2)
            if not doc_func:
                doc_func = legacy["testcase_func_doc"]

        doc_func = doc_func or default_doc_func
        name_func = name_func or default_name_func

        def parameterized_expand_wrapper(f):
            frame_locals = inspect.currentframe().f_back.f_locals

            parameters = parameterized.input_as_callable(input_values)()

            if not parameters:
                if not skip_on_empty:
                    raise ValueError(
                        "Parameters iterable is empty (hint: use "
                        "`parameterized.expand([], skip_on_empty=True)` to skip "
                        "this test when the input_class is empty)"
                    )
                from functools import wraps
                return wraps(f)(skip_on_empty_helper)

            digits = len(str(len(parameters) - 1))
            for num, p in enumerate(parameters):
                name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)

                nf = reapply_patches_if_need(f)
                # if attrs is not None:
                #     frame_locals[name] = parameterized.param_as_standalone_func_attrs(p, nf, name, attrs)
                # else:
                frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
                frame_locals[name].__doc__ = doc_func(f, num, p)

            # Delete original patches to prevent new function from evaluating
            # original patching object as well as re-constructed patches.
            delete_patches_if_need(f)

            f.__test__ = False
            return f

        return parameterized_expand_wrapper

    @classmethod
    def data_class(cls, attrs, input_values=None):
        """
        通过在类上设置属性来参数化测试类
        :param attrs: 类属性
        :param input_values: 参数化数据
        """
        return parameterized_class(attrs, input_values=input_values)

    def data_api(self, url: str = None, method='GET', params: dict = None, json: dict = None, headers: dict = None,
                 ret: str = None):
        """
        支持接口数据参数化
        :param json:  json参数
        :param method:  请求方式
        :param url: 接口地址
        :param params: 接口参数
        :param headers: 接口请求头
        :param ret: 接口返回值, 用于提取数据, 例如: ret="result"

        {
          "success":true,
          "error": {
            "code":"",
            "message":""
          },
          "result":[
            {
              "scene": "测试1",
              "email": "li123@126.com",
              "password": "abc123"
            },
            {
              "scene": "测试2",
              "email": "li456@126.com",
              "password": "abc456"
            }
          ]
        }
        """

        if url is None and weeeConfig.data_api_url is None:
            raise ValueError("url is not None")
        # method 转大写
        method = method.upper()
        http = HttpRequest()
        # 如果参数化的url不是以http开头, 则拼接配置文件中的url
        http_url = url
        if (weeeConfig.data_api_url is not None) and (url.startswith("http") is False):
            http_url = weeeConfig.data_api_url + url

        # 根据请求方式, 发送请求
        if method == "GET":
            resp = http.get(http_url, params=params, headers=headers).json()
        elif method == "POST":
            resp = http.post(http_url, params=params, headers=headers, json=json).json()
        elif method == "PUT":
            resp = http.put(http_url, params=params, headers=headers, json=json).json()
        elif method == "DELETE":
            resp = http.delete(http_url, params=params, headers=headers, json=json).json()
        else:
            raise ValueError("method is GET/POST/PUT/DELETE")

        log.debug("api参数化接口返回json为: %s", resp)
        log.debug("json提取数据为: %s", ret)

        if ret is not None:
            # 提取数据

            data_ = jmespath(resp, ret)
            if data_ is None:
                # 如果提取的数据为空, 则抛出异常
                raise ValueError(f"Error - return {ret} is None in {resp}")
            if isinstance(data_, list) is False:
                # 如果提取的数据不是列表, 则抛出异常
                raise TypeError(f"Error - {data_} is not list")

            return self.data(data_)

        if isinstance(resp, list) is False:
            # 如果返回的数据不是列表, 则抛出异常
            raise TypeError(f"Error - {resp} is not list")
        # 返回数据
        return self.data(resp)


params = Parameters()
