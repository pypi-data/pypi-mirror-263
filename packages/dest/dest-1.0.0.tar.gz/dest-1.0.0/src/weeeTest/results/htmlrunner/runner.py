import datetime
import json
import os
import sys
import unittest
from xml.sax import saxutils

from jinja2 import Environment, FileSystemLoader

from weeeTest import version
from weeeTest.config import RunResult, Message
from weeeTest.results._email import SMTP
from weeeTest.results._weixin import Weixin
from weeeTest.version import get_version

# default tile
DEFAULT_TITLE = 'seeTestRunner Test Report'

# ---------------------------
# Define the HTML template directory
# --------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_DIR = os.path.join(BASE_DIR, "html")

env = Environment(loader=FileSystemLoader(HTML_DIR))
if RunResult.language == "en":
    TEMPLATE_HTML = "./template/email/en/template_en.html"
elif RunResult.language == "zh-CN":
    TEMPLATE_HTML = "./template/email/zh/template_zh.html"
else:
    raise EnvironmentError("The language is not supported")

if RunResult.language == "en":
    STYLESHEET_HTML = "./template/email/en/stylesheet_en.html"
elif RunResult.language == "zh-CN":
    STYLESHEET_HTML = "./template/email/zh/stylesheet_zh.html"
else:
    raise EnvironmentError("The language is not supported")


class CustomTemplate:
    """
    Define a HTML template for results customerization and generation.
    Overall structure of an HTML results
    """

    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
        3: 'skip',
    }

    REPORT_CLASS_TMPL = r"""
    <tr class='%(style)s'>
        <td>%(name)s</td>
        <td>%(desc)s</td>
        <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">%(detail_button_text)s</a></td>
    </tr>
    """  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_CASE_TMPL = r"""
    <tr class='%(style)s'>
        <td>%(name)s</td>
        <td>%(desc)s</td>
        <td>%(case_type)s</td>
         <td>%(run_time)s  s</td>
        <td>%(status)s</td>
        <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">%(detail_button_text)s</a></td>
    </tr>
    """  # variables: (style, desc, count, Pass, fail, error, cid)
    REPORT_CASE_TMPL_DEV = r"""
        <tr class='%(style)s'>
            <td>%(desc)s</td>
            <td>%(name)s</td>
            <td>%(url)s</td>
            <td>%(request)s</td>
            <td>%(response)s</td>
            <td>%(case_type)s</td>
             <td class='nowrap'>%(run_time)s  s</td>
            <td class='nowrap'>
        <!--css div popup start-->
        <a class="popup_link" href="javascript:void(0)" onclick="showLog('div_%(cid)s')">%(status)s</a>
        <div id='div_%(cid)s' class="modal show" style="display: none; background-color: #000000c7;">
            <div class="modal-dialog modal-dialog-centered log_window">
                <div class="modal-content shadow-3">
                    <div class="modal-header">
                        <div>
                            <h5 class="mb-1">%(log_title)s</h5>
                        </div>
                        <div>
                            <h5 class="mb-1">detailed log</h5>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-square bg-tertiary bg-opacity-20 bg-opacity-100-hover text-tertiary text-white-hover" data-bs-dismiss="modal" onclick="hideLog('div_%(cid)s')">X</button>
                        </div>
                    </div>
                    <div class="modal-body">
                        <div>
                            <pre>%(script)s</pre>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--css div popup end-->
    </td>
            <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">%(detail_button_text)s</a></td>
        </tr>
        """  # variables: (style, desc, count, Pass, fail, error, cid)
    REPORT_CASE_TMPL_DEV_NO_DETAIL = r"""
        <tr class='%(style)s'>
        <td>%(desc)s</td>
            <td>%(name)s</td>
            <td>%(url)s</td>
            <td>%(request)s</td>
            <td>%(response)s</td> 
            <td>%(case_type)s</td>
             <td class='nowrap'>%(run_time)s  s</td>
            <td class='nowrap'>
        <!--css div popup start-->
        <a class="popup_link" href="javascript:void(0)" onclick="showLog('div_%(cid)s')">%(status)s</a>
        <div id='div_%(cid)s' class="modal show" style="display: none; background-color: #000000c7;">
            <div class="modal-dialog modal-dialog-centered log_window">
                <div class="modal-content shadow-3">
                    <div class="modal-header">
                        <div>
                            <h5 class="mb-1">%(log_title)s</h5>
                        </div>
                        <div>
                            <h5 class="mb-1">detailed log</h5>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-square bg-tertiary bg-opacity-20 bg-opacity-100-hover text-tertiary text-white-hover" data-bs-dismiss="modal" onclick="hideLog('div_%(cid)s')">X</button>
                        </div>
                    </div>
                    <div class="modal-body">
                        <div>
                            <pre>%(script)s</pre>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--css div popup end-->
    </td>
            <td></td>
        </tr>
        """  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'>
        <div class='testcase'>%(casename)s</div>
    </td>
    <td style="color: #495057">
        <div>%(desc)s</div>
    </td>
    <td style="color: #495057">
        <div>%(runtime)s s</div>
    </td>
    <td colspan='5' align='center' class='caseStatistics'>
        <!--css div popup start-->
        <a class="popup_link" href="javascript:void(0)" onclick="showLog('div_%(tid)s')">%(status)s</a>
        <div id='div_%(tid)s' class="modal show" style="display: none; background-color: #000000c7;">
            <div class="modal-dialog modal-dialog-centered log_window">
                <div class="modal-content shadow-3">
                    <div class="modal-header">
                        <div>
                            <h5 class="mb-1">%(log_title)s</h5>
                        </div>
                        <div>
                            <h5 class="mb-1">detailed log</h5>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-square bg-tertiary bg-opacity-20 bg-opacity-100-hover text-tertiary text-white-hover" data-bs-dismiss="modal" onclick="hideLog('div_%(tid)s')">X</button>
                        </div>
                    </div>
                    <div class="modal-body">
                        <div>
                            <pre>%(script)s</pre>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--css div popup end-->
    </td>
    <td>%(img)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'>
        <div class='testcase'>%(casename)s</div>
    </td>
    <td style="color: #495057">
        <div>%(desc)s</div>
    </td>
    <td style="color: #495057">
        <div>%(runtime)s s</div>
    </td>
    <td colspan='5' align='center'>%(status)s</td>
    <td>%(img)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL_DEV = r"""
    <tr id='%(tid)s' class='%(Class)s'>
        <td></td>
        <td></td>
        <td style="color: #495057">
            <div>%(url)s</div>
        </td>
        <td style="color: #495057">
            <div>%(request)s</div>
        </td>
        <td style="color: #495057">
            <div>%(response)s</div>
        </td>
        
    </tr>
    """  # variables: (tid, Class, style, desc, status)

    IMG_TMPL = r"""
<a onfocus='this.blur();' href="javascript:void(0)" onclick="showImg(this)">show</a>
<div id="case-image" class="modal show" style="display:none; background-color: #000000c7;">
  <div class="modal-dialog modal-dialog-centered log_window">
    <div class="modal-content shadow-3">
      <div class="modal-header">
        <div>
          <h5 class="mb-1">screenshots</h5>
        </div>
          <div>
            <button class="btn btn-sm btn-square bg-tertiary bg-opacity-20 bg-opacity-100-hover text-tertiary text-white-hover" onclick='hideImg(this)'">X</button>
          </div>
        </div>
        <div class="modal-body" style="height: 600px; background: #e7eaf0;">
          {images}
        </div>
        <div class="img-circle"></div>
    </div>
    </div>
</div>
"""


class HTMLTestRunner(object):
    """
    Run the test class
    """

    def __init__(self,
                 stream=sys.stdout,
                 verbosity=1,
                 title=None,
                 tester="Anonymous",
                 description=None,
                 save_last_run=True,
                 language=None,  # en/ zh-CN
                 logger=None,
                 **kwargs):
        self.stream = stream
        self.verbosity = verbosity
        self.save_last_run = save_last_run
        self.run_times = 0
        self.logger = logger
        if language is not None:
            RunResult.language = language
        if title is None:
            self.title = DEFAULT_TITLE
        else:
            self.title = title
        RunResult.title = self.title
        self.tester = tester
        RunResult.tester = tester
        if description is None:
            self.description = ""
        elif isinstance(description, str):
            self.description = description
        elif isinstance(description, list):
            self.description = ""
            for desc in description:
                p_tag = '<p>' + desc + '</p>'
                self.description = self.description + p_tag
        else:
            self.description = ""

        self.start_time = datetime.datetime.now()
        self.end_time = None
        self.test_obj = None

        self.whitelist = set(kwargs.pop('whitelist', []))
        self.blacklist = set(kwargs.pop('blacklist', []))

    @classmethod
    def test_iter(cls, suite):
        """
        Iterate through test suites, and yield individual tests
        """
        for test in suite:
            if isinstance(test, unittest.TestSuite):
                for t in cls.test_iter(test):
                    yield t
            else:
                yield test

    def generate_report(self, result_header_json: str, result_case_json: str):
        template = env.get_template(TEMPLATE_HTML)
        stylesheet = env.get_template(STYLESHEET_HTML).render()
        # base, statistics = self.get_report_attributes(result) header_result = '{"base": {"title": "测试报告test","start_time": "2023-03-23 17:09:25","end_time": "2023-03-23 19:09:25","duration": "0:00:08.031","tester": "tester_test","description": "测试报告description"},
        # "total": {"pass_num": 10,"pass_percent":"10%","fail_num": 2,"fail_percent":"1%","error_num": 1,"error_percent":"10%","skip_num": 0,"skip_percent":"10%"}}'
        header_result = json.loads(result_header_json)
        # version = '1.0'
        heading = self._generate_heading(header_result)
        # 遍历结果集
        report = self._generate_report(result_case_json)

        html_content = template.render(
            title=saxutils.escape(header_result['base']['title']),
            version=get_version,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            channel=self.run_times,
        )
        self.stream.write(html_content.encode('utf8'))

    def generate_report_dev(self, result_header_json: str, result_case_json: str):
        template = env.get_template(TEMPLATE_HTML)
        stylesheet = env.get_template(STYLESHEET_HTML).render()
        # base, statistics = self.get_report_attributes(result) header_result = '{"base": {"title": "测试报告test","start_time": "2023-03-23 17:09:25","end_time": "2023-03-23 19:09:25","duration": "0:00:08.031","tester": "tester_test","description": "测试报告description"},
        # "total": {"pass_num": 10,"pass_percent":"10%","fail_num": 2,"fail_percent":"1%","error_num": 1,"error_percent":"10%","skip_num": 0,"skip_percent":"10%"}}'
        header_result = json.loads(result_header_json)
        # version = '1.0'
        heading = self._generate_heading_dev(header_result)
        # 遍历结果集
        report = self._generate_report_dev(result_case_json)

        html_content = template.render(
            title=saxutils.escape(header_result['base']['title']),
            version=get_version,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            channel=self.run_times,
        )
        self.stream.write(html_content.encode('utf8'))

    # 7月7号：_generate_heading与_generate_heading_dev改为一样了。
    @staticmethod
    def _generate_heading(header_result: dict):
        if RunResult.language == "en":
            heading_html = "./template/email/en/heading_en.html"
        elif RunResult.language == "zh-CN":
            heading_html = "./template/email/zh/heading_zh.html"
        else:
            raise EnvironmentError("The language is not supported")

        heading = env.get_template(heading_html).render(
            title=header_result["base"]["title"],
            start_time=header_result["base"]["start_time"],
            end_time=header_result["base"]["end_time"],
            duration=header_result["base"]["duration"],
            tester=header_result["base"]["tester"],
            description=header_result["base"]["description"],
            platform=header_result["base"]["platform"] if header_result.get('base').get("platform") else "无平台信息",
            version=header_result["base"]["version"] if header_result.get('base').get("version") else "无版本信息",
            app=header_result["base"]["app"] if header_result.get('base').get("app") else "无应用信息",
            p_number=header_result["total"]["pass_num"],
            p_percent=header_result["total"]["pass_percent"],
            f_number=header_result["total"]["fail_num"],
            f_percent=header_result["total"]["fail_percent"],
            e_number=header_result["total"]["error_num"],
            e_percent=header_result["total"]["error_percent"],
            s_number=header_result["total"]["skip_num"],
            s_percent=header_result["total"]["skip_percent"],
        )
        return heading

    @staticmethod
    def _generate_heading_dev(header_result: dict):
        if RunResult.language == "en":
            heading_html = "./template/email/en/heading_en.html"
        elif RunResult.language == "zh-CN":
            heading_html = "./template/email/zh/heading_zh_dev.html"
        else:
            raise EnvironmentError("The language is not supported")

        heading = env.get_template(heading_html).render(
            title=header_result["base"]["title"],
            start_time=header_result["base"]["start_time"],
            end_time=header_result["base"]["end_time"],
            duration=header_result["base"]["duration"],
            tester=header_result["base"]["tester"],
            description=header_result["base"]["description"],
            platform=header_result["base"]["platform"] if header_result.get('base').get("platform") else "无平台信息",
            version=header_result["base"]["version"] if header_result.get('base').get("version") else "无版本信息",
            app=header_result["base"]["app"] if header_result.get('base').get("app") else "无应用信息",
            p_number=header_result["total"]["pass_num"],
            p_percent=header_result["total"]["pass_percent"],
            f_number=header_result["total"]["fail_num"],
            f_percent=header_result["total"]["fail_percent"],
            e_number=header_result["total"]["error_num"],
            e_percent=header_result["total"]["error_percent"],
            s_number=header_result["total"]["skip_num"],
            s_percent=header_result["total"]["skip_percent"],
        )
        return heading

    def _generate_report(self, result_case_json: str):
        rows = []

        # result_case_json = '[{"case_name": "case-name1","desc": "case-desc1","status": 0,"run_time": "0.1","case_detail": [{"step_name": "setup","case_desc": "setup_desc","run_time": "0.02","status": 1,"out_message": "","error_message": "错误日志"},{"step_name": "test_01","case_desc": "test_01_desc","run_time": "0.01","status": 1,"out_message": "输出日志","error_message": "错误日志"},{"step_name": "teardown","case_desc": "teardown_desc","run_time": "0.01","status": 2,"out_message": "输出日志","error_message": "错误日志"}]},{"case_name": "case-name2","desc": "case-desc2","status": 1,"run_time": "0.1","case_detail": [{"step_name": "setup01","case_desc": "setup_desc","run_time": "0.01","status": 0,"out_message": "输出日志","error_message": ""},{"step_name": "test_02","case_desc": "test_02_desc","run_time": "0.01","status": 1,"out_message": "输出日志","error_message": "错误日志"},{"step_name": "teardown","case_desc": "teardown_desc","run_time": "0.01","status": 2,"out_message": "输出日志","error_message": "错误日志"}]}]'
        result_case_List = json.loads(result_case_json)
        num_pass = num_fail = num_error = num_skip = 0
        cid = -1
        for case in result_case_List:
            cid += 1
            case_status = case['status']
            if case_status == 0:
                num_pass += 1
            elif case_status == 1:
                num_fail += 1
            elif case_status == 2:
                num_error += 1
            else:
                num_skip += 1
            if RunResult.language == "en":
                detail_button_text = 'detail'
            else:
                detail_button_text = '详情'
            row = CustomTemplate.REPORT_CASE_TMPL % dict(
                style=case['status'] == 0 and "passClass" or (case['status'] == 1 and 'failClass' or (
                        case['status'] == 2 and 'errorClass' or 'skipClass')),
                # style='passClass',
                name=case['case_name'],
                desc=case['desc'],
                case_type=case['case_type'] if case.get('case_type') else "",
                run_time=case['run_time'],
                count=len(list(case['case_detail'])),
                status=CustomTemplate.STATUS[case['status']],
                detail_button_text=detail_button_text,
                cid='c.{}'.format(cid + 1),
            )
            # print("cid:::",cid)
            rows.append(row)
            tid = -1
            for step in case['case_detail']:
                tid += 1
                if step["status"] == 0:
                    tmp = "p"
                elif step["status"] == 1:
                    tmp = "f"
                elif step["status"] == 2:
                    tmp = "e"
                else:
                    tmp = "s"
                # print("tid:::", tid)
                self._generate_report_test(rows, cid=cid, tid=tid, num=step['status'], test=step['step_name'],
                                           out=step['out_message'],
                                           error=step['error_message'], run_time=step['run_time'],
                                           desc=step['step_desc'])

        # 最后渲染
        if RunResult.language == "en":
            report_html = "./template/email/en/body_en.html"
        elif RunResult.language == "zh-CN":
            report_html = "./template/email/zh/body_zh.html"
        else:
            raise EnvironmentError("The language is not supported")
        report = env.get_template(report_html).render(
            test_list=''.join(rows),
            count=str(num_pass + num_fail + num_error + num_skip),
            Pass=str(num_pass),
            fail=str(num_fail),
            error=str(num_error),
            skip=str(num_skip),
            channel=str(self.run_times),
        )
        return report

    def _generate_report_dev(self, result_case_json: str):
        rows = []

        # result_case_json = '[{"case_name": "case-name1","desc": "case-desc1","status": 0,"run_time": "0.1","case_detail": [{"step_name": "setup","case_desc": "setup_desc","run_time": "0.02","status": 1,"out_message": "","error_message": "错误日志"},{"step_name": "test_01","case_desc": "test_01_desc","run_time": "0.01","status": 1,"out_message": "输出日志","error_message": "错误日志"},{"step_name": "teardown","case_desc": "teardown_desc","run_time": "0.01","status": 2,"out_message": "输出日志","error_message": "错误日志"}]},{"case_name": "case-name2","desc": "case-desc2","status": 1,"run_time": "0.1","case_detail": [{"step_name": "setup01","case_desc": "setup_desc","run_time": "0.01","status": 0,"out_message": "输出日志","error_message": ""},{"step_name": "test_02","case_desc": "test_02_desc","run_time": "0.01","status": 1,"out_message": "输出日志","error_message": "错误日志"},{"step_name": "teardown","case_desc": "teardown_desc","run_time": "0.01","status": 2,"out_message": "输出日志","error_message": "错误日志"}]}]'
        result_case_List = json.loads(result_case_json)
        num_pass = num_fail = num_error = num_skip = 0
        cid = -1
        for case in result_case_List:
            cid += 1
            case_status = case['status']
            if case_status == 0:
                num_pass += 1
            elif case_status == 1:
                num_fail += 1
            elif case_status == 2:
                num_error += 1
            else:
                num_skip += 1
            if RunResult.language == "en":
                detail_button_text = 'detail'
            else:
                detail_button_text = '详情'
                # case处url显示
            url_context = case['url'] if case.get('url') else (
                "共有 " + str(len(list(case['case_detail']))) + " 个请求接口" if len(
                    list(case['case_detail'])) > 0 else "无请求接口")
            if case['case_detail']:
                row = CustomTemplate.REPORT_CASE_TMPL_DEV % dict(
                    style=case['status'] == 0 and "passClass" or (case['status'] == 1 and 'failClass' or (
                            case['status'] == 2 and 'errorClass' or 'skipClass')),
                    # style='passClass',
                    name=case['case_name'],
                    # case处url显示
                    url=url_context,
                    request=case['request'] if case.get('request') else "",
                    response=case['response'] if case.get('response') else "",
                    desc=case['desc'],
                    case_type=case['case_type'] if case.get('case_type') else "",
                    run_time=case['run_time'],
                    count=len(list(case['case_detail'])),
                    status=CustomTemplate.STATUS[case['status']],
                    detail_button_text=detail_button_text,
                    cid='c.{}'.format(cid + 1),
                    log_title=case['case_name'][case['case_name'].rfind("::") + 2:],
                    script="""out_message:{out}\n\nerror_message:{error}""".format(
                        out=case['out_message'] if case.get("out_message") else "无out_message",
                        error=case['error_message'] if case.get("error_message") else "无error_message")
                )
            else:
                row = CustomTemplate.REPORT_CASE_TMPL_DEV_NO_DETAIL % dict(
                    style=case['status'] == 0 and "passClass" or (case['status'] == 1 and 'failClass' or (
                            case['status'] == 2 and 'errorClass' or 'skipClass')),
                    # style='passClass',
                    name=case['case_name'],
                    url=url_context,
                    request=case['request'] if case.get('request') else "",
                    response=case['response'] if case.get('response') else "",
                    desc=case['desc'],
                    case_type=case['case_type'] if case.get('case_type') else "",
                    run_time=case['run_time'],
                    count=len(list(case['case_detail'])),
                    status=CustomTemplate.STATUS[case['status']],
                    cid='c.{}'.format(cid + 1),
                    log_title=case['case_name'][case['case_name'].rfind("::") + 2:],
                    script="""out_message:{out}\n\nerror_message:{error}""".format(
                        out=case['out_message'] if case.get("out_message") else "无out_message",
                        error=case['error_message'] if case.get("error_message") else "无error_message")
                )
            # print("cid:::",cid)
            rows.append(row)
            tid = -1
            for step in case['case_detail']:
                tid += 1
                # if step["status"] == 0:
                #     tmp = "p"
                # elif step["status"] == 1:
                #     tmp = "f"
                # elif step["status"] == 2:
                #     tmp = "e"
                # else:
                #     tmp = "s"
                # print("tid:::", tid)
                self._generate_report_test_dev(rows, cid=cid, tid=tid, url=step['url'], request=step['request'],
                                               response=step['response'])

        # 最后渲染
        if RunResult.language == "en":
            report_html = "./template/email/en/body_en.html"
        elif RunResult.language == "zh-CN":
            report_html = "./template/email/zh/body_zh_dev.html"
        else:
            raise EnvironmentError("The language is not supported")
        report = env.get_template(report_html).render(
            test_list=''.join(rows),
            count=str(num_pass + num_fail + num_error + num_skip),
            Pass=str(num_pass),
            fail=str(num_fail),
            error=str(num_error),
            skip=str(num_skip),
            channel=str(self.run_times),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, num, test, out, error, run_time, desc):
        # e.g. 'pt1.1', 'ft1.1','et1.1', 'st1.1' etc
        has_output = bool(out or error)
        if num == 0:
            tmp = "p"
        elif num == 1:
            tmp = "f"
        elif num == 2:
            tmp = "e"
        else:
            tmp = "s"
        tid = tmp + 't{}.{}'.format(cid + 1, tid + 1)
        # tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        # name = test.id().split('.')[-1]
        name = test
        # doc = test.shortDescription() or ""
        # doc = desc
        # desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and CustomTemplate.REPORT_TEST_WITH_OUTPUT_TMPL or CustomTemplate.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(out, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formatting
            # uo = unicode(o.encode('string_escape'))
            uo = out
        else:
            uo = out
        if isinstance(error, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formatting
            # ue = unicode(e.encode('string_escape'))
            ue = error
        else:
            ue = error
        script = """out_message:{out}\n\nerror_message:{error}""".format(
            # id=tid,
            # output=saxutils.escape(uo + ue),
            out=out,
            error=error
        )
        # add image
        if getattr(test, 'images', []):
            tmp = ""
            for i, img in enumerate(test.images):
                if i == 0:
                    tmp += """<img src="data:image/jpg;base64,{}" style="display: block;" class="img"/>\n""".format(img)
                else:
                    tmp += """<img src="data:image/jpg;base64,{}" style="display: none;" class="img"/>\n""".format(img)
            screenshots_html = CustomTemplate.IMG_TMPL.format(images=tmp)
        else:
            screenshots_html = """"""

        # add runtime
        # if getattr(test, 'runtime', []):
        #     runtime = test.runtime
        # else:
        #     runtime = "0.00"

        row = tmpl % dict(
            tid=tid,
            # Class=(num == 0 and 'hiddenRow' or 'none'),
            Class='hiddenRow',
            style=num == 2 and 'errorCase' or (num == 1 and 'failCase' or 'passCase'),
            casename=name,
            desc=desc,
            runtime=run_time,
            log_title=name,
            script=script,
            status=CustomTemplate.STATUS[num],
            img=screenshots_html
        )
        rows.append(row)
        rows.append(row)
        if not has_output:
            return

    def _generate_report_test_dev(self, rows, cid, tid, url, request, response):
        # e.g. 'pt1.1', 'ft1.1','et1.1', 'st1.1' etc
        # has_output = bool(out or error)
        # if num == 0:
        #     tmp = "p"
        # elif num == 1:
        #     tmp = "f"
        # elif num == 2:
        #     tmp = "e"
        # else:
        #     tmp = "s"
        tid = "p" + 't{}.{}'.format(cid + 1, tid + 1)
        # tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        # name = test.id().split('.')[-1]
        # name = test
        # doc = test.shortDescription() or ""
        # doc = desc
        # desc = doc and ('%s: %s' % (name, doc)) or name
        # tmpl = has_output and CustomTemplate.REPORT_TEST_WITH_OUTPUT_TMPL_DEV or CustomTemplate.REPORT_TEST_NO_OUTPUT_TMPL_DEV
        tmpl = CustomTemplate.REPORT_TEST_NO_OUTPUT_TMPL_DEV

        # o and e should be byte string because they are collected from stdout and stderr?
        # if isinstance(out, str):
        #     # uo = unicode(o.encode('string_escape'))
        #     uo = out
        # else:
        #     uo = out
        # if isinstance(error, str):
        #     # ue = unicode(e.encode('string_escape'))
        #     ue = error
        # else:
        #     ue = error
        # script = """out_message:{out}\n\nerror_message:{error}""".format(
        #     # id=tid,
        #     # output=saxutils.escape(uo + ue),
        #     out=out,
        #     error=error
        # )
        # # add image
        # if getattr(test, 'images', []):
        #     tmp = ""
        #     for i, img in enumerate(test.images):
        #         if i == 0:
        #             tmp += """<img src="data:image/jpg;base64,{}" style="display: block;" class="img"/>\n""".format(img)
        #         else:
        #             tmp += """<img src="data:image/jpg;base64,{}" style="display: none;" class="img"/>\n""".format(img)
        #     screenshots_html = CustomTemplate.IMG_TMPL.format(images=tmp)
        # else:
        #     screenshots_html = """"""

        # add runtime
        # if getattr(test, 'runtime', []):
        #     runtime = test.runtime
        # else:
        #     runtime = "0.00"

        row = tmpl % dict(
            tid=tid,
            # Class=(num == 0 and 'hiddenRow' or 'none'),
            Class='hiddenRow',
            # style=num == 2 and 'errorCase' or (num == 1 and 'failCase' or 'passCase'),
            style='passCase',
            # casename=name,
            # desc=desc,
            # runtime=run_time,
            # log_title=name,
            # script=script,
            # status=CustomTemplate.STATUS[num],
            # img=screenshots_html,
            url=url if url else "",
            request=request if request else "",
            response=response if response else "",
        )
        rows.append(row)
        rows.append(row)
        # if not has_output:
        #     return

    @staticmethod
    def send_email(to: any, attachments=None):
        """
        Send test result to email
        :param to:
        :param attachments:
        :return:
        """
        SMTP(user=Message.user, password=Message.password, host=Message.host, port=Message.port).sender(to=to,
                                                                                                        attachments=attachments)

    @staticmethod
    def send_weixin():
        """
        Send test result to
        :return:
        """
        Weixin().send_wx_message()
