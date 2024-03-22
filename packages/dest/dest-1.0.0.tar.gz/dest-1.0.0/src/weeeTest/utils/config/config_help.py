# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Jialing chen
@Version        :  V1.0.0
------------------------------------
@File           :  config_help.py
@Description    :  
@CreateTime     :  2023/4/20 10:47
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/20 10:47
"""
import re
from contextlib import closing

import boto3
from spring_config import ClientConfigurationBuilder
from spring_config.client import SpringConfigClient


def get_spring_config(profile: str, file_name: str) -> dict:
    config = (
        ClientConfigurationBuilder()
        .profile(profile)
        .app_name(file_name)  # config file
        .address("http://config.tb1.sayweee.net:8888")
        .authentication(('user', 'triple@xian'))
        .build()
    )

    c = SpringConfigClient(config)
    return c.get_config()
    # print(type(c.get_config()),c.get_config())
    # print(json.dumps(c.get_config()))


def get_info_from_manager(secret_name: str) -> str:
    boto_session = boto3.session.Session(region_name='us-west-2')
    with closing(boto_session.client('secretsmanager')) as secret_client:
        secret_value_response = secret_client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in secret_value_response:
            secret_value = secret_value_response['SecretString']
            return secret_value
        else:
            raise AttributeError('could not get config from secrets manager. conf_id: %s')


# 递归方式替换占位符
def replace_placeholder(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                # 使用正则表达式匹配占位符变量名
                placeholders = re.findall(r'\${(.*?)}', value)
                for placeholder in placeholders:
                    # 替换占位符变量
                    data[key] = value.replace(f'${{{placeholder}}}', get_info_from_manager(placeholder))
            else:
                replace_placeholder(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                replace_placeholder(item)
            elif isinstance(item, str):
                # 处理字符串
                placeholders = re.findall(r'\${(.*?)}', item)
                for placeholder in placeholders:
                    data[i] = item.replace(f'${{{placeholder}}}', get_info_from_manager(placeholder))


# 本地调试
def replace_placeholder_test(data, variables):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                # 使用正则表达式匹配占位符变量名
                placeholders = re.findall(r'\${(.*?)}', value)
                for placeholder in placeholders:
                    # 替换占位符变量
                    if placeholder in variables:
                        value = value.replace(f'${{{placeholder}}}', variables[placeholder])
                data[key] = value
            else:
                replace_placeholder_test(value, variables)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                replace_placeholder_test(item, variables)
            elif isinstance(item, str):
                # 处理字符串
                placeholders = replace_placeholder_test.findall(r'\${(.*?)}', item)
                for placeholder in placeholders:
                    if placeholder in variables:
                        item = item.replace(f'${{{placeholder}}}', variables[placeholder])
                data[i] = item


if __name__ == '__main__':
    # config_dict = get_spring_config(profile="central", file_name="weee-fp-data")
    # value_dict = {"spring_datasource_password": "123456qqq"}
    # replace_placeholder(config_dict, value_dict)
    # print(json.dumps(config_dict))

    # local
    # config_dict = get_spring_config(profile="local", file_name="weee-qa")
    # print('config_dict...', config_dict)
    # small_dict = {}
    # small_dict['db_ec'] = config_dict['datasource']['ec']
    # small_dict['db_wms'] = config_dict['datasource']['wms']
    # print('222...', json.dumps(small_dict))
    # values = {
    #     'db_erp_username': 'weee_auto_test',
    #     'db_erp_password': '&!w1vgEJHW6fsTEb',
    #     'db_wms_username': 'weee_auto_test',
    #     'db_wms_password': '&!w1vgEJHW6fsTEb',
    # }
    # replace_placeholder_test(small_dict, values)
    # print(json.dumps(small_dict))
    # sql = "select userId,username from weee.user limit 2"
    # ec_dict = small_dict['db_ec']
    # with MysqlUtil(host=ec_dict['host'], user=ec_dict['username'], password=ec_dict['password'],
    #                port=ec_dict['port']) as conn:
    #     ret = asyncio.run(MysqlUtil.execute_query(conn, sql_str=sql))
    #     print(ret, type(ret))
    print("获取secret-manager信息")
    print('db_erp_username:::', get_info_from_manager(secret_name='db_erp_username'))
    print('db_erp_password:::', get_info_from_manager(secret_name='db_erp_password'))
    print('db_wms_username:::', get_info_from_manager(secret_name='db_wms_username'))
    print('db_wms_password:::', get_info_from_manager(secret_name='db_wms_password'))
