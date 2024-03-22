# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Yingqing Shan
@Version        :  V1.0.0
------------------------------------
@File           :  push_help.py
@Description    :  
@CreateTime     :  2023/3/31 13:36
@Software       :  PyCharm
------------------------------------
@ModifyTime     :  2023/3/31 13:36
"""
import os

from weeeTest.config import weeeConfig
from weeeTest.results import Weixin, SMTP as XSMTP
from weeeTest.utils import file


class EmailSMTP(XSMTP):
    """send email class"""

    def sendmail(self, to: [str, list], subject: str = None, attachments: str = None, delete: bool = False) -> None:
        """
        seldom send email
        :param to:
        :param subject:
        :param attachments:
        :param delete: delete report&log file
        :return
        """
        if attachments is None:
            attachments = weeeConfig.report_path
        if subject is None:
            subject = weeeConfig.report_title
        self.sender(to=to, subject=subject, attachments=attachments)
        if delete is True:
            file.remove(weeeConfig.report_path)
            is_exist = os.path.isfile(weeeConfig.log_path)
            if is_exist is True:
                with open(weeeConfig.log_path, "r+", encoding="utf-8") as log_file:
                    log_file.truncate(0)


class Weinxin(Weixin):
    """
    send weixin Class
    """
    pass
