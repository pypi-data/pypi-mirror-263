import os.path

from weeeTest.config import Message
from weeeTest.results.htmlrunner.runner import HTMLTestRunner


class Report:
    def __init__(self, report: str = None):

        if report is not None and len(report) > 0:
            if not report.endswith(".html"):
                self.report = report + ".html"
            else:
                self.report = report
        else:
            raise Exception('report不能为空')

    def generate_report(self, header_result_json: str, result_case_json: str):
        # 生成测试报告
        with(open(self.report, 'wb')) as fp:
            self.runner = HTMLTestRunner(stream=fp)
            self.runner.generate_report(header_result_json, result_case_json)
        return os.path.abspath(self.report)

    # 给开发看的报告
    def generate_report_dev(self, header_result_json: str, result_case_json: str):
        # 生成测试报告
        report_dev_path = self.report[:self.report.rfind('.')]
        report_dev_path = report_dev_path + "_dev.html"
        with(open(report_dev_path, 'wb')) as fp:
            self.runner = HTMLTestRunner(stream=fp)
            self.runner.generate_report_dev(header_result_json, result_case_json)
        return report_dev_path

    def send(self, send_type="email", to=None):
        if send_type == "weixin":
            HTMLTestRunner().send_weixin()
        elif send_type == "email":
            if to:
                HTMLTestRunner.send_email(to=to, attachments=self.report)
        else:
            print(f"{send_type} is unavailable, send failed!")


if __name__ == '__main__':
    # 邮件
    case_re = '''{
	"base": {
		"title": "weeeTest 自带 Demo",
		"start_time": "2023-06-27 18:37:20",
		"end_time": "2023-06-27 18:37:20",
		"duration": "00:00:00",
		"tester": "yingqing.shan",
		"description": "weeeTest 自带 Demo",
		"platform":"jenkins",
		"version":"0.0.1",
		"app":"ec"
	},
	"total": {
		"pass_num": 4,
		"pass_percent": "100.0%",
		"fail_num": 0,
		"fail_percent": "0.0%",
		"error_num": 0,
		"error_percent": "0.0%",
		"skip_num": 0,
		"skip_percent": "0.0%"
	}
}'''
    case_details = '''[
    {
        "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_xls",
        "desc": "desc1",
        "status": 0,
        "run_time": 0.0745,
        "url":"",
        "request":"",
        "response":"",
        "case_detail": []
    },
    {
        "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_yaml",
        "desc": "desc2",
        "status": 1,
        "run_time": 0.0041,
        "url":"",
        "request":"",
        "response":"",
        "out_message": "新out22",
        "error_message": "新error11",
        "case_detail": [
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_yaml",
                "step_name": "SetUp",
                "step_desc": "",
                "status": 1,
                "run_time": 0.0002,
                "out_message": "out22",
                "error_message": "error11",
                "url":"www.sayweee1.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
            },
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_yaml",
                "step_name": "Call",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0038,
                "out_message": "",
                "error_message": "",
                "url":"www.sayweee1.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
            },
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_yaml",
                "step_name": "TearDown",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0001,
                "out_message": "",
                "error_message": "",
                "url":"www.sayweee1.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
            }
        ]
    },
    {
        "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_csv",
        "desc": "desc3",
        "status": 0,
        "run_time": 0.0028,
        "url":"",
        "request":"",
        "response":"",
        "case_detail": [
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_csv",
                "step_name": "SetUp",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0002,
                "out_message": "",
                "error_message": "",
                "url":"www.sayweee1.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
            },
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_csv",
                "step_name": "Call",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0025,
                "out_message": "",
                "error_message": "",
                "url":"www.sayweee1.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
            },
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_csv",
                "step_name": "TearDown",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0001,
                "out_message": "",
                "error_message": "",
                 "url":"www.sayweee1.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
            }
        ]
    },
    {
        "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_json",
        "desc": "desc",
        "status": 0,
        "run_time": 0.0017,
        "case_detail": [
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_json",
                "step_name": "SetUp",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0002,
                "out_message": "",
                "error_message": "",
                "url":"www.baidu.com",
                "request":"484884838388488883883884848383288388848484848838848388489999999",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkZZZZZZ"
            },
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_json",
                "step_name": "Call",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0013,
                "out_message": "",
                "error_message": "",
                "url":"www.google.com",
                "request":"484884838388488883883884848383288388848484848838848388486666666",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkQQQ"
            },
            {
                "case_name": "test_dir/data_case/test_data/test_file_demo.py::TestFileDemo::test_read_json",
                "step_name": "TearDown",
                "step_desc": "",
                "status": 0,
                "run_time": 0.0002,
                "out_message": "",
                "error_message": "",
                "url":"www.sayweee.com",
                "request":"48488483838848888388388484838328838884848484883884838848777777",
                "response":"jdjfjdjfjdjjfjdfjdjfjdjfjdjjdjfjjdkekekekkekekekkkddkkUUUUU"
                
            }
        ]
    }
]'''
    report = Report(report="reports/report11.html")
    report.generate_report_dev(case_re, case_details)
    report.generate_report(case_re, case_details)
