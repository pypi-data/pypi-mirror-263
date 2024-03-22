# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  mark.py
@Description    :  
@CreateTime     :  2023/4/25 17:48
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/25 17:48
"""

import pytest

called_test_cases = {}


class Mark:

    @staticmethod
    def parametrize(*args, **kwargs):
        """
        参数化
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.parametrize(*args, **kwargs)

    @staticmethod
    def skip(*args, **kwargs):
        """
        跳过
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.skip(*args, **kwargs)

    @staticmethod
    def skipif(*args, **kwargs):
        """
        跳过
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.skipif(*args, **kwargs)

    @staticmethod
    def xfail(*args, **kwargs):
        """
        预期失败
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.xfail(*args, **kwargs)

    @staticmethod
    def xfailif(*args, **kwargs):
        """
        预期失败
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.xfailif(*args, **kwargs)

    @staticmethod
    def usefixtures(*args, **kwargs):
        """
        使用fixture
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.usefixtures(*args, **kwargs)

    @staticmethod
    def dependency(*args, **kwargs):
        """
        依赖
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.dependency(*args, **kwargs)

    @staticmethod
    def order(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.order(*args, **kwargs)

    @staticmethod
    def run(order):
        """
        顺序
        :param order:
        :return:
        """
        return pytest.mark.run(order=order)

    @staticmethod
    def run_after(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_after(*args, **kwargs)

    @staticmethod
    def run_before(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_before(*args, **kwargs)

    @staticmethod
    def run_these(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_these(*args, **kwargs)

    @staticmethod
    def run_first(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_first(*args, **kwargs)

    @staticmethod
    def run_last(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_last(*args, **kwargs)

    @staticmethod
    def run_only(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only(*args, **kwargs)

    @staticmethod
    def run_only_if(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if(*args, **kwargs)

    @staticmethod
    def run_only_if_not(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not(*args, **kwargs)

    @staticmethod
    def run_only_if_env(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_env(*args, **kwargs)

    @staticmethod
    def run_only_if_not_env(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not_env(*args, **kwargs)

    @staticmethod
    def run_only_if_in(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_in(*args, **kwargs)

    @staticmethod
    def run_only_if_not_in(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not_in(*args, **kwargs)

    @staticmethod
    def run_only_if_os(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_os(*args, **kwargs)

    @staticmethod
    def run_only_if_not_os(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not_os(*args, **kwargs)

    @staticmethod
    def run_only_if_python(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_python(*args, **kwargs)

    @staticmethod
    def run_only_if_not_python(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not_python(*args, **kwargs)

    @staticmethod
    def run_only_if_module(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_module(*args, **kwargs)

    @staticmethod
    def run_only_if_not_module(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not_module(*args, **kwargs)

    @staticmethod
    def run_only_if_program(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_program(*args, **kwargs)

    @staticmethod
    def run_only_if_not_program(*args, **kwargs):
        """
        顺序
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.run_only_if_not_program(*args, **kwargs)

    @staticmethod
    def timeout(*args, **kwargs):
        """
        超时
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.mark.timeout(*args, **kwargs)

    @staticmethod
    def fixture(*args, **kwargs):
        """
        fixture
        :param args:
        :param kwargs:
        :return:
        """
        return pytest.fixture(*args, **kwargs)

    @staticmethod
    def list(*args):
        """
        将多个自定义标记转成单个标记
        示例：weeeTest.mark.list("Simple", "P0", "Smoke")
        :return:
        """

        def decorator(func):
            for arg in args:
                marker = getattr(pytest.mark, arg)
                func = marker(func)
            return func

        return decorator

    @staticmethod
    def simple(*args, **kwargs):
        def decorator(func):
            # setattr(func, "__decorators__", args)
            func.__annotations__['case_type'] = 'simple'
            pytest.mark.simple(*args, **kwargs)
            return func

        return decorator

    @staticmethod
    def scene(*args, **kwargs):
        def decorator(func):
            # setattr(func, "__decorators__", args)
            func.__annotations__['case_type'] = 'scene'
            pytest.mark.simple(*args, **kwargs)
            return func

        return decorator


mark = Mark()
