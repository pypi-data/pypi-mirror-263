import json
from typing import Any

from deepdiff import DeepDiff

from weeeTest.utils import log


class AssertInfo:
    warning = []
    error = []


def diff_json(response_data: Any, assert_data: Any, exclude: list = None) -> None:
    """
    Compare the JSON data format
    """
    if exclude is None:
        exclude = []

    if isinstance(response_data, dict) and isinstance(assert_data, dict):
        # dict format
        for key in assert_data:
            # skip check
            if key in exclude:
                continue
            if key not in response_data:
                AssertInfo.error.append(f"❌ Response data has no key: {key}")
        for key in response_data:
            # skip check
            if key in exclude:
                continue
            if key in assert_data:
                # recursion
                diff_json(response_data[key], assert_data[key], exclude)
            else:
                AssertInfo.warning.append(f"💡 Assert data has not key: {key}")
    elif isinstance(response_data, list) and isinstance(assert_data, list):
        # list format
        if len(response_data) == 0:
            log.info("response is []")
        else:
            if isinstance(response_data[0], dict):
                try:
                    response_data = sorted(response_data, key=lambda x: x[list(response_data[0].keys())[0]])
                except TypeError:
                    response_data = response_data
            else:
                response_data = sorted(response_data)

        if len(response_data) != len(assert_data):
            log.info(f"list len: '{len(response_data)}' != '{len(assert_data)}'")

        if len(assert_data) > 0:
            if isinstance(assert_data[0], dict):
                try:
                    assert_data = sorted(assert_data, key=lambda x: x[list(assert_data[0].keys())[0]])
                except TypeError:
                    assert_data = assert_data
            else:
                assert_data = sorted(assert_data)

        for src_list, dst_list in zip(response_data, assert_data):
            # recursion
            diff_json(src_list, dst_list, exclude)
    else:
        # different format
        if str(response_data) != str(assert_data):
            AssertInfo.error.append(f"❌ Value are not equal: {assert_data} != {response_data}")


def json_diff(json_one, json_two) -> dict:
    """
    :param json_one: 支持str，dict
    :param json_two: 支持str，dict
    :return: 返回差异化字典
    """
    dict1 = {}
    dict2 = {}
    if isinstance(json_one, str):
        dict1 = json.loads(json_one)
    elif isinstance(json_one, dict):
        dict1 = json_one
    else:
        raise Exception('json_one格式错误,只支持str,dict格式')

    if isinstance(json_two, str):
        dict2 = json.loads(json_two)
    elif isinstance(json_two, dict):
        dict2 = json_two
    else:
        raise Exception('json_one格式错误,只支持str,dict格式')
    return dict(DeepDiff(dict1, dict2))


def mysql_results_diff(result_list1: list, result_list2: list) -> dict:
    """
    mysql结果集比对
    :param result_list1: 数据库查询结果集：list类型
    :param result_list2: 数据库查询结果集：list类型
    :return: 返回字典：lines；diff_list
    """
    dict_return = {}
    if len(result_list1) != len(result_list2):
        dict_return['lines'] = 'list行数不相等,result_list1::' + str(len(result_list1)) + ",result_list2::" + str(
            len(result_list2))
        return dict_return
    else:
        diff_list = []
        for i in range(len(result_list1)):
            dict1 = dict(result_list1[i])
            dict2 = dict(result_list2[i])
            diff_list.append(json_diff(dict1, dict2))
        dict_return['lines'] = len(result_list1)
        dict_return['diff_list'] = diff_list
        return dict_return


if __name__ == '__main__':
    # json比对
    jsonThree = "{\"msgtype\":\"text\",\"text\":{\"content\":\"\",\"mentioned_mobile_list\":\"\"}}"
    jsonFour = "{\"text\":{\"content\":\"\"}}"
    print(json_diff(jsonThree, jsonFour))

    # mysqllist比对
    # sql = "select id,name,age from student  ORDER BY id desc limit 2"
    # conn = MysqlUtil('localhost', 'root', '123456', 'test_db', 3306, 'json')
    # ret1 = asyncio.run(
    #     MysqlUtil.execute_query(conn, sql_str=sql))
    # print(ret1, type(ret1))
    #
    # print('---------------------')
    # sql = "select id,name,age from student  ORDER BY id desc limit 2,1"
    # conn = MysqlUtil('localhost', 'root', '123456', 'test_db', 3306, 'json')
    # ret2 = asyncio.run(
    #     MysqlUtil.execute_query(conn, sql_str=sql))
    # print(ret2, type(ret2))
    #
    # diff = mysql_results_diff(json.loads(ret1), json.loads(ret2))
    # print('mysql-result-list', diff)
