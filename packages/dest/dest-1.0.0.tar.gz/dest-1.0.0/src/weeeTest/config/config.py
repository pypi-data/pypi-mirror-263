# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  config.py
@Description    :  
@CreateTime     :  2023/3/30 11:14
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/30 11:14
"""
import time


class weeeConfig:
    """
    配置文件
    """
    timeout = 10
    debug = False
    base_url = None
    env = 'local'  # 执行环境 local、tb1-根据这个字段读取：springcloud config
    project = 'ec'  # 项目：ec、erp、wms
    db_config = {}  # 连接数据库的配置信息，来源springcloud config
    DB_CONFIG_EC_KEY = "db_ec"
    DB_CONFIG_WMS_KEY = "db_wms"

    report_path = None
    report_title = "weeeTest Test Report"
    report_tester = "weeeTest"
    report_description = "weeeTest Test Report"

    # 日志路径
    log_path = None

    # 用例路径
    test_dir = 'test_dir'

    # 测试数据文件夹名称
    test_data_dir_name = 'test_data'

    # 项目根目录
    project_root_dir = None

    # 接口测试数据地址
    data_api_url = None

    # 调用test开头函数测试用例列表
    run_call_test_fun_name_list = []

    # 流程用例相关单接口case
    called_test_cases = {}


class RunResult:
    """
    Test run results
    """
    language = "zh-CN"  # en/ zh-CN
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    end_time = time.strftime("%Y-%m-%d %H:%M:%S")
    duration = "00:00:00"
    passed = 0
    failed = 0
    errors = 0
    skipped = 0
    pass_rate = '0.00%'
    failure_rate = '0.00%'
    error_rate = '0.00%'
    skip_rate = '0.00%'

    # 每个用例的执行结果
    DEV_EVERY_CASES_RESULT = []
    # 每个用例的请求结果
    DEV_EVERY_CASES_RES = []

    # 当前执行的用例名称
    CURRENT_CASE_NAME = None


class Message:
    # weixin
    access_token = None  # 机器人token
    at_mobiles = [13700000000]  # 需要@人的手机号
    append = None
    text = None
    is_at_all = False
    is_text = False

    # email
    user = "ops.qa@sayweee.com"  # 邮箱账号
    password = "mmzsblayzfaeflby"  # 邮箱授权码
    host = "smtp.gmail.com"
    to = None  # 收件人
    to_dev = None  # 开发人员收件人
    port = "465"
