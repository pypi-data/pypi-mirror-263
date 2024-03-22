# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  __init__.py.py
@Description    :  
@CreateTime     :  2023/3/22 14:39
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/22 14:39
"""
import json
import os
import time
import webbrowser
from collections import defaultdict

import pytest

from weeeTest import log, Message, log_cfg
from weeeTest.config import weeeConfig, RunResult
from weeeTest.results.send_report import Report
from weeeTest.utils.config.config_help import get_spring_config, replace_placeholder

CASE_DETAIL = []  # 用例详情
# 每个用例的执行结果
EVERY_CASES_RESULT = []


def get_case_type(func, case_name: str):
    case_type = func.__annotations__.get("case_type")

    if case_type:
        return case_type
    elif "simple" in case_name.split("::")[0].lower():
        return "simple"
    elif "scene" in case_name.split("::")[0].lower():
        return "scene"
    else:
        return "other"


def pytest_addoption(parser):
    parser.addini("base_url", "请求URL", default="")
    parser.addini("env", "环境", default="")
    parser.addini("project", "项目", default="")
    parser.addini("title", "标题", default="")
    parser.addini("tester", "测试人", default="")
    parser.addini("description", "描述", default="")
    parser.addini("language", "语言", default="")


def pytest_configure(config):
    # 获取测试用例目录路径
    test_dir_path = config.rootdir
    weeeConfig.project_root_dir = test_dir_path
    log.debug("执行文件或命令来自终端,获取的项目目录为：{}".format(test_dir_path))
    # 从pytest.ini中获取
    for key, value in config.inicfg.items():
        if key == 'base_url':
            weeeConfig.base_url = value
        elif key == 'env':
            weeeConfig.env = value
            if value.lower().strip() == 'local':
                config_dict = get_spring_config(profile="local", file_name="weee-qa")
                weeeConfig.db_config[weeeConfig.DB_CONFIG_EC_KEY] = config_dict['datasource']['ec']
                weeeConfig.db_config[weeeConfig.DB_CONFIG_WMS_KEY] = config_dict['datasource']['wms']
            elif value.lower().strip() == 'tb1':
                config_dict = get_spring_config(profile="central", file_name="weee-qa")
                weeeConfig.db_config[weeeConfig.DB_CONFIG_EC_KEY] = config_dict['datasource']['ec']
                weeeConfig.db_config[weeeConfig.DB_CONFIG_WMS_KEY] = config_dict['datasource']['wms']
                # 连接secret manager替换占位符
                replace_placeholder(weeeConfig.db_config)
            else:
                raise Exception(f"不支持的环境{value.lower().strip()}")
            log.info(f'db配置信息...{weeeConfig.db_config}')
        elif key == 'project':
            # 读取springcloud config
            weeeConfig.project = value
        elif key == 'title':
            weeeConfig.report_title = value
        elif key == 'tester':
            weeeConfig.report_tester = value
        elif key == 'description':
            weeeConfig.report_description = value
        elif key == 'language':
            RunResult.language = value
        elif key == 'weixin_access_token':
            Message.access_token = value
        elif key == 'email_to':
            Message.to = value
        elif key == 'email_to_dev':
            Message.to_dev = value
        elif key == 'debug':
            if value:
                print('日志等级debug')
                log_cfg.set_level(level='DEBUG')
            else:
                log_cfg.set_level(level='INFO')
        elif key == 'report_path':
            if (config.inicfg['report_path'] is None) and (weeeConfig.report_path is not None):
                weeeConfig.report_path = weeeConfig.report_path
            else:
                report = str(weeeConfig.report_path).replace('\\', '/')
                report_file_name = report[report.rfind('/') + 1:len(report)]
                log.debug(f'成功从配置文件中获取文件名{report_file_name}')
                path = os.path.join(os.getcwd(), "reports", weeeConfig.report_path)
                if not os.path.exists(path):
                    os.makedirs(path)
                weeeConfig.report_path = os.path.join(path, report_file_name)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    #     """
    #     用例执行结果 hook 函数
    #     :param item:
    #     :param call:
    #     :return:
    #     """

    result = yield
    if result.get_result().when == 'teardown':
        # 收集allure装饰器信息
        report = result.get_result()
        fixture_extras = getattr(item.config, "extras", [])
        plugin_extras = getattr(report, "extra", [])
        report.extra = fixture_extras + plugin_extras

        # 获取用例模块名，例如：
        # @allure.epic("对象存储")
        # @allure.story("桶")
        # @allure.feature("对象")
        module_dict = defaultdict(str)
        if hasattr(item.instance, 'pytestmark'):
            for pm in item.instance.pytestmark:
                if 'label_type' in pm.kwargs:
                    module_dict[pm.kwargs["label_type"]] = pm.args[0]
        for om in item.own_markers:
            if 'label_type' in om.kwargs:
                module_dict[om.kwargs["label_type"]] = om.args[0]

        # 三级模块
        module_name_v3 = [
            {"epic": module_dict['epic'],
             "feature": module_dict['feature'],
             "story": module_dict['story'],
             }
        ]

        print("allure装饰器信息:::", module_name_v3)

    # case结果汇总
    report = result.get_result()
    _case_nodeid = item.nodeid  # 获取用例函数的名称

    step_status = 0  # 0：成功，1：失败，2：错误，3：跳过
    out_message = ''  # 输出信息
    error_message = ''  # 错误信息
    step_desc = ''  # 步骤描述
    case_name = item.nodeid  # 获取用例函数的名称
    dev_case_name = item.originalname  # 获取用例函数的名称
    RunResult.CURRENT_CASE_NAME = item.originalname
    desc = '' if item.function.__doc__ is None else item.function.__doc__  # 获取用例函数的名称的文档
    run_time = round(report.duration, 4)  # 获取用例setup执行时间

    if report.when == 'setup':
        step_name = "SetUp"
        if report.outcome == 'passed':
            step_status = 0  # 0：成功，1：失败，2：错误，3：跳过

        elif report.outcome == 'failed':
            step_status = 2  # 0：成功，1：失败，2：错误，3：跳过
            out_message = str(call.excinfo.value)  # 获取用例执行失败的输出信息
            error_message = report.longreprtext  # 获取用例执行失败的错误信息
            log.error('\n异常信息: {}'.format(call.excinfo.value))
            log.error('\n详细异常错误定位: {}'.format(report.longreprtext))
        elif report.outcome == 'skipped':
            step_status = 3  # 0：成功，1：失败，2：错误，3：跳过

        # 测试开发报告详情
        CASE_DETAIL.append(
            {"case_name": case_name, "step_name": step_name, "step_desc": step_desc, "status": step_status,
             "run_time": run_time, "out_message": out_message, "error_message": error_message})

    elif report.when == 'call':
        step_name = "Call"
        if report.outcome == 'passed':
            step_status = 0  # 0：成功，1：失败，2：错误，3：跳过
        elif report.outcome == 'failed':
            step_status = 1  # 0：成功，1：失败，2：错误，3：跳过
            out_message = str(call.excinfo.value)  # 获取用例执行失败的输出信息
            error_message = report.longreprtext  # 获取用例执行失败的错误信息
            log.error('\n用例异常信息：{}'.format(call.excinfo.value))
            log.error('\n详细异常错误定位：{}'.format(report.longreprtext))
        # 测试开发报告详情
        CASE_DETAIL.append(
            {"case_name": case_name, "step_name": step_name, "step_desc": step_desc, "status": step_status,
             "run_time": run_time, "out_message": out_message, "error_message": error_message})


    elif report.when == 'teardown':
        step_name = "TearDown"
        if report.outcome == 'passed':
            step_status = 0  # 0：成功，1：失败，2：错误，3：跳过
        elif report.outcome == 'failed':
            step_status = 2  # 0：成功，1：失败，2：错误，3：跳过
            out_message = str(call.excinfo.value)  # 获取用例执行失败的输出信息
            error_message = report.longreprtext  # 获取用例执行失败的错误信息
            log.error('\n后置条件异常: {}'.format(call.excinfo.value))
            log.error('\n详细异常错误定位: {}'.format(report.longreprtext))
        elif report.outcome == 'skipped':
            step_status = 3  # 0：成功，1：失败，2：错误，3：跳过

        # 测试报告详情
        CASE_DETAIL.append(
            {"case_name": case_name, "step_name": step_name, "step_desc": step_desc, "status": step_status,
             "run_time": run_time, "out_message": out_message, "error_message": error_message})

        # ************************* >> 用例执行结果处理  << *******************************
        # ************************* >> 测试人员报告数据处理 start << **************************
        case_details = []  # 用例详情列表
        case_status = 0  # 0：成功，1：失败，2：错误，3：跳过
        run_time_sum = 0  # 用例执行时间总和

        for i in CASE_DETAIL:
            if i['case_name'] == case_name:
                case_details.append(i)  # 将用例详情添加到用例详情列表

        for i in case_details:  # 遍历用例详情列表
            run_time_sum += i['run_time']  # 获取用例执行时间总和
            if i['status'] == 2:  # 如果用例详情列表中的用例状态为2，即用例错误
                case_status = 2
                break
            elif i['status'] == 1:  # 如果用例详情列表中的用例状态为1，即用例失败
                case_status = 1
                break
            elif i['status'] == 3:  # 如果用例详情列表中的用例状态为3，即用例跳过
                case_status = 3
                break
            else:  # 如果用例详情列表中的用例状态为3，即用例跳过
                num = 0
                num += 1

        # case_type = item.function.__annotations__.get("case_type")
        case_type = get_case_type(func=item.function, case_name=item.nodeid)
        # 测试报告每个用例结果
        EVERY_CASES_RESULT.append(
            {"case_name": case_name, "desc": desc, "status": case_status, "run_time": round(run_time_sum, 4),
             "case_detail": case_details, "case_type": case_type})  # 每个用例的结果

        # ******************** >> 测试人员报告数据处理 end  << **************************

        # ******************** >> 开发数据处理 start << **************************

        dev_case_details = []  # 用例详情列表

        dev_out_message = ''  # 开发者输出信息
        dev_error_message = ''  # 开发者错误信息

        # 开发报告详情
        for i in RunResult.DEV_EVERY_CASES_RES:  # 遍历用例详情列表
            if i['case_name'] == dev_case_name:
                dev_case_details.append(i)  # 将用例详情添加到用例详情列表
        for i in CASE_DETAIL:
            if i['case_name'] == case_name:
                if i['status'] == 0:  # 如果用例详情列表中的用例状态为0，即用例成功
                    # 将数据添加到dev测试报告数据列表中
                    if len(i['out_message']) > 0:
                        dev_out_message = '\n' + i['step_name'] + ':\n' + i['out_message']

                if i['status'] == 2:  # 如果用例详情列表中的用例状态为2，即用例错误
                    # 将数据添加到dev测试报告数据列表中
                    if len(i['error_message']) > 0:
                        dev_out_message = '\n' + i['step_name'] + ':\n' + i['out_message']
                        dev_error_message = '\n' + i['step_name'] + ':\n' + i['error_message']
                elif i['status'] == 1:  # 如果用例详情列表中的用例状态为1，即用例失败
                    # 将数据添加到dev测试报告数据列表中
                    if len(i['error_message']) > 0:
                        dev_out_message = '\n' + i['step_name'] + ':\n' + i['out_message']
                        dev_error_message = '\n' + i['step_name'] + ':\n' + i['error_message']
                elif i['status'] == 3:  # 如果用例详情列表中的用例状态为3，即用例跳过
                    # 将数据添加到dev测试报告数据列表中
                    if len(i['out_message']) > 0:
                        dev_out_message = '\n' + i['step_name'] + ':\n' + i['out_message']

        # 开发测试报告每个用例结果
        RunResult.DEV_EVERY_CASES_RESULT.append(
            {"case_name": dev_case_name, "desc": desc, "status": case_status, "run_time": round(run_time_sum, 4),
             "case_detail": dev_case_details, "out_message": dev_out_message,
             "error_message": dev_error_message})  # 每个用例的结果

        # ******************** >> 开发报告数据处理 end << **************************


def pytest_terminal_summary(terminalreporter, config):
    """
    收集测试结果
    """
    pytest_total_num = terminalreporter._numcollected
    pass_num = len(terminalreporter.stats.get('passed', []))  # 用例通过数
    fail_num = len(terminalreporter.stats.get('failed', []))  # 用例失败数
    error_num = len(terminalreporter.stats.get('error', []))  # 用例错误数
    skip_num = len(terminalreporter.stats.get('skipped', []))  # 用例跳过数
    RunResult.end_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 测试结束时间
    RunResult.duration = time.strftime("%H:%M:%S",
                                       time.gmtime(time.time() - terminalreporter._sessionstarttime))  # 测试耗时转换成时分秒
    RunResult.passed = pass_num  # 用例通过数
    RunResult.failed = fail_num  # 用例失败数
    RunResult.errors = error_num  # 用例错误数
    RunResult.skipped = skip_num  # 用例跳过数
    total_num = pass_num + fail_num + error_num + skip_num  # 用例总数
    if total_num != 0:
        RunResult.pass_rate = str(round(pass_num / total_num * 100, 2)) + '%'  # 用例通过率
        RunResult.skip_rate = str(round(skip_num / total_num * 100, 2)) + '%'  # 用例跳过率
        RunResult.failure_rate = str(round(fail_num / total_num * 100, 2)) + '%'  # 用例失败率
        RunResult.error_rate = str(round(error_num / total_num * 100, 2)) + '%'  # 用例错误率
    else:
        RunResult.pass_rate = '0.00%'
        RunResult.skip_rate = '0.00%'
        RunResult.failure_rate = '0.00%'
        RunResult.error_rate = '0.00%'

    def get_base_data():
        return {
            "title": weeeConfig.report_title,
            "start_time": RunResult.start_time,
            "end_time": RunResult.end_time,
            "duration": RunResult.duration,
            "tester": weeeConfig.report_tester,
            "description": weeeConfig.report_description
        }

    def get_total_data():
        return {
            "pass_num": RunResult.passed,
            "pass_percent": RunResult.pass_rate,
            "fail_num": RunResult.failed,
            "fail_percent": RunResult.failure_rate,
            "error_num": RunResult.errors,
            "error_percent": RunResult.error_rate,
            "skip_num": RunResult.skipped,
            "skip_percent": RunResult.skip_rate,
        }

    # Jenkins 参加合并报告汇总数据
    platform = os.getenv("upstream_env", None)
    upstream_branch = os.getenv("upstream_branch", None)
    upstream_build_number = os.getenv("upstream_build_number", None)
    if upstream_branch is not None and upstream_build_number is not None:
        version = upstream_branch + '[' + upstream_build_number + ']'
    else:
        version = None
    app = os.getenv("upstream_app", None)

    CASE_RESULT = {
        "base": {
            **get_base_data(),
            "platform": platform,
            "version": version,
            "app": app,
        },
        "total": get_total_data(),
    }

    # 测试报告测试
    case_re = json.dumps(CASE_RESULT, ensure_ascii=False, indent=4)  # 用例结果转换成json格式
    case_details = json.dumps(EVERY_CASES_RESULT, ensure_ascii=False, indent=4)  # 用例详情转换成json格式
    # 测试报告处理
    dev_case_details = json.dumps(RunResult.DEV_EVERY_CASES_RESULT, ensure_ascii=False, indent=4)  # 用例详情转换成json格式

    report = Report(weeeConfig.report_path)  # 实例化Report类
    # 开发报告日志
    log.debug('weeeTest插件获取测试报告路径: {}'.format(weeeConfig.report_path))
    log.debug('weeeTest插件执行结果汇总json数据: {}'.format(case_re))
    log.debug('weeeTest插件执行结果详情json数据: {}'.format(case_details))
    # 开发报告详情日志
    log.debug('weeeTest插件执行结果详情dev的json数据: {}'.format(dev_case_details))

    # 提示信息
    if pytest_total_num != total_num:
        log.error(
            f'注意：weeeTest获取到用例数量为：{pytest_total_num}个, 实际执行的用例数量为：{total_num}个不一致, 请检查用例是否全部被执行。')

    if error_num > 0:
        log.error(f'注意：weeeTest执行错误用例数量为：{error_num}个, 请检查用例代码是否有错.')

    if fail_num > 0:
        log.error(f'注意：weeeTest执行断言用例数量为：{fail_num}个, 请检查断言是否有误.')

    report.generate_report(case_re, case_details)  # 测试开发测试报告生成
    report.generate_report_dev(case_re, dev_case_details)  # 开发测试报告生成

    # 发送邮件
    if Message.to is not None and len(Message.to) > 0:
        report = Report(report=weeeConfig.report_path)
        report.send(send_type='email', to=Message.to)

    # 发送微信
    if Message.access_token is not None and len(Message.access_token) > 0:
        report = Report(report=weeeConfig.report_path)
        report.send(send_type='weixin')

    if os.path.exists(weeeConfig.report_path):
        log.success(f"generated html file: file:///{weeeConfig.report_path}")
        webbrowser.open_new(f"file:///{weeeConfig.report_path}")

    else:
        log.error(f"generated html file: file:///{weeeConfig.report_path} is not exist")
        log.debug(f"未安装 weeeTest 插件，可使用 pip install weeeTest 安装")

    log.success(f"generated log file: file:///{weeeConfig.log_path}")


@pytest.fixture(scope="session", autouse=True)
def user_setup():
    RunResult.start_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 测试开始时间
    yield
