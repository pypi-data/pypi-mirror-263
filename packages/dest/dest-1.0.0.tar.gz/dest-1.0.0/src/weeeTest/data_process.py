# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  data_process.py
@Description    :  
@CreateTime     :  2023/4/19 16:58
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/4/19 16:58
"""

from weeeTest.testdata.common.file.parameterization import FileData
from weeeTest.testdata.common.mysql import MysqlCommon
from weeeTest.testdata.common.redis.parameterization import RedisCommon


class DataProcess:
    """
    数据处理类
    """

    def mysql(self, sql: str, return_type: str = None, **db_conn):
        """
        mysql数据处理
        :param sql:  sql语句
        :param db_conn_env:  数据库连接环境
        :param return_type:  返回数据类型
        :param db_conn:  数据库连接参数
        :return:
        """
        return MysqlCommon().mysql(sql=sql, return_type=return_type, db_conn=db_conn)

    @classmethod
    def redis(cls, key: str, value=None, redis_conn_env: str = 'local', expire_time: int = -1,
              **redis_conn):
        """
        redis数据处理
        :param key:  redis的key
        :param value:  redis的value
        :param redis_conn_env:  redis连接环境
        :param return_type:  返回数据类型
        :param expire_time:  过期时间
        :param redis_conn:  redis连接参数
        :return:
        """
        return RedisCommon().redis(key=key, value=value, redis_conn_env=redis_conn_env,
                                   expire_time=expire_time, redis_conn=redis_conn)

    @classmethod
    def file(cls, file_name: str, do_type: str = 'read', return_type: str = None, sheet: str = "Sheet1",
             start_line: int = 1, end_line: int = None, test_data_dir_name: str = 'test_data'):
        """
        文件数据处理
        :param file_name: 文件名称
        :param do_type: 操作类型
        :param return_type: 返回数据类型
        :param sheet: sheet名称
        :param start_line: 读取的起始行
        :param end_line: 读取的结束行
        :param test_data_dir_name 测试数据文件夹名称
        :return:
        """
        return FileData().file_data(file_name=file_name, do_type=do_type, return_type=return_type,
                                    sheet=sheet, line=start_line, end_line=end_line,
                                    test_data_dir_name=test_data_dir_name)


data = DataProcess()

__all__ = ['data']
