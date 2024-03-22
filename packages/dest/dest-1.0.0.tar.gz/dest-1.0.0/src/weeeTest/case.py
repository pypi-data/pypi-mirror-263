# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  case.py
@Description    :
@CreateTime     :  2023/3/22 12:18
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/22 12:18
"""

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from weeeTest.testdata.common.diff import AssertInfo, diff_json
from weeeTest.testdata.common.request import HttpRequest, formatting, ResponseResult
from weeeTest.utils import check
from weeeTest.utils import jmespath, log


class TestCase(HttpRequest):
    """
    Base class for test cases.
    """

    @staticmethod
    def assert_status_code(status_code: int, msg: str = None) -> None:
        """
        断言状态码是否符合预期一致
        :arg status_code: 预期状态码
        :arg msg: 断言失败时的提示信息
        """
        log.info(f"👀 assertStatusCode -> {status_code}.")
        check.assert_equal(ResponseResult.status_code, status_code, msg=msg)

    @staticmethod
    def assert_schema(schema, response=None) -> None:
        """
        断言响应json数据每个字段的类型是否与给定的类型一直
        文档: https://json-schema.org/
        :arg schema: json 模型
        :arg response: 响应数据
        """
        log.info(f"👀 assertSchema -> {formatting(schema)}.")

        if response is None:
            response = ResponseResult.response

        try:
            validate(instance=response, schema=schema)
        except ValidationError as msg:
            check.assert_equal("Response data", "Schema data", msg=msg.message)

    @staticmethod
    def assert_json(assert_json, response=None, exclude=None) -> None:
        """
        断言响应json数据是否符合预期一致
        :arg assert_json: 预期json数据
        :arg response: 响应数据
        :arg exclude: 排除字段
        """
        log.info(f"👀 assertJSON -> {assert_json}.")
        if response is None:
            response = ResponseResult.response

        AssertInfo.warning = []
        AssertInfo.error = []
        diff_json(response, assert_json, exclude)
        if len(AssertInfo.warning) != 0:
            log.warning(AssertInfo.warning)
        if len(AssertInfo.error) != 0:
            check.assert_equal("Response data", "Assert data", msg=AssertInfo.error)

    @staticmethod
    def assert_json_path(path, value) -> None:
        """
        按照路径断言响应json数据是否符合预期一致
        文档: https://jmespath.org/
        :arg path: 路径
        :arg value: 预期值
        """
        log.info(f"👀 assertPath -> {path} >> {value}.")
        search_value = jmespath(ResponseResult.response, path)
        check.assert_equal(search_value, value, msg=f"Path: {path} >> {search_value} != {value}.")

    @staticmethod
    def assert_equal(actual, expected, msg=None) -> None:
        """
        断言两个值是否相等
        :arg actual: 实际值
        :arg expected: 预期值
        :arg msg: 断言失败时的提示信息
        """
        log.info(f"👀 assertEqual -> {actual} >> {expected}.")
        check.assert_equal(actual, expected, msg=msg)
