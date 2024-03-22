import os

import requests
from jinja2 import Environment, FileSystemLoader

from weeeTest.config import Message, RunResult, weeeConfig
from weeeTest.utils import log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")
env = Environment(loader=FileSystemLoader(HTML_DIR))


class Weixin:
    """
    SendNail group notification
    help doc:
        https://developer.work.weixin.qq.com/document/path/91770
    """

    def __init__(self):

        self.url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={Message.access_token}"
        self.at_mobiles = Message.at_mobiles
        self.is_at_all = Message.is_at_all
        self.is_text = Message.is_text
        self.append = Message.append
        self.text = Message.text

    @staticmethod
    def _get_weixin_notice_content():
        """
        get notice content
        """
        if RunResult.language == "en":
            notice_tmp = "./template/push/en/notice_en.md"
        elif RunResult.language == "zh-CN":
            notice_tmp = "./template/push/zh/notice_zh.md"
        else:
            raise EnvironmentError("The language is not supported")
        res_text = env.get_template(notice_tmp).render(
            title=weeeConfig.report_title,
            tester=weeeConfig.report_tester,
            start_time=RunResult.start_time,
            end_time=RunResult.end_time,
            duration=RunResult.duration,
            p_number=RunResult.passed,
            pass_rate=RunResult.pass_rate,
            f_number=RunResult.failed,
            failure_rate=RunResult.failure_rate,
            e_number=RunResult.errors,
            error_rate=RunResult.error_rate,
            s_number=RunResult.skipped,
            skip_rate=RunResult.skip_rate,
        )
        return res_text

    @staticmethod
    def _send_message(wx_url: str, data: dict):
        """
        发送微信消息
        :param wx_url: webhooks加密后地址
        :param data: 消息详情
        :return:
        """
        headers = {"Content-Type": "application/json"}
        log.debug(wx_url)
        log.debug(dict(data))
        result = requests.post(wx_url, headers=headers, json=dict(data))
        return result.json()

    def send_wx_message(self):
        """
        Send weixin message push
        :return:
        """
        if Message.access_token is None or len(Message.access_token) == 0:
            raise Exception('access_token为空，无法发送微信')
        if self.is_at_all is True:
            self.at_mobiles.append("@all")
        res_text = self._get_weixin_notice_content()

        if self.append is not None:
            res_text = res_text + str(self.append)
        if self.text is not None:
            res_text = self.text

        if self.is_text is True:
            message = {"msgtype": "text", "text": {"content": res_text, "mentioned_mobile_list": self.at_mobiles}}
        else:
            message = {"msgtype": "markdown", "markdown": {"content": res_text}}

        resp = self._send_message(self.url, message)
        if resp["errcode"] == 0:
            log.info(" 📧 weixin sent successfully!!")
        else:
            log.error("❌ weixin failed to send!!")
            log.error(resp)
        return resp
