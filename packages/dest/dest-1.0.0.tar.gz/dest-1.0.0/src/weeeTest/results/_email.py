import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

from weeeTest.config import weeeConfig, RunResult
from weeeTest.utils import log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")
INIT_FILE = os.path.join(BASE_DIR, "__init__.py")
env = Environment(loader=FileSystemLoader(HTML_DIR))


class SMTP(object):
    """
    Mail function based on EmailSMTP protocol
    """

    def __init__(self, user, password, host, port=None):
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def sender(self, to=None, subject=None, contents=None, attachments=None):
        if to is None or len(to) == 0:
            raise ValueError("Please specify the email address to send")
        log.info(f"email-host::{self.host}")
        log.info(f"email-port::{self.port}")
        if isinstance(to, str):
            to = to.split(',')
            for i in range(len(to)):
                item = to[i]
                if "@" not in item:
                    item += '@sayweee.com'
                    to[i] = item

        if isinstance(to, list) is False:
            raise ValueError("Received mail type error")

        if subject is None:
            subject = weeeConfig.report_title
        if contents is None:
            if RunResult.language == "en":
                mail_tem = './template/email/en/mail_en.html'
            elif RunResult.language == "zh-CN":
                mail_tem = "./template/email/zh/mail_zh.html"
            else:
                raise EnvironmentError("The language is not supported")
            contents = env.get_template(mail_tem).render(
                mail_title=str(weeeConfig.report_title),
                start_time=str(RunResult.start_time),
                end_time=str(RunResult.end_time),
                mail_tester=str(weeeConfig.report_tester),
                duration=str(RunResult.duration),
                mail_pass=str(RunResult.passed),
                pass_rate=str(RunResult.pass_rate),
                mail_fail=str(RunResult.failed),
                failure_rate=str(RunResult.failure_rate),
                mail_error=str(RunResult.errors),
                error_rate=str(RunResult.error_rate),
                mail_skip=str(RunResult.skipped),
                skip_rate=str(RunResult.skip_rate)
            )

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.user
        msg['To'] = ",".join(to)
        log.debug(f"发送人：：{msg['To']}")
        text = MIMEText(contents, 'html', 'utf-8')
        msg.attach(text)

        if attachments is not None:
            att_name = "results.html"
            if "\\" in attachments:
                att_name = attachments.split("\\")[-1]
            if "/" in attachments:
                att_name = attachments.split("/")[-1]

            att = MIMEApplication(open(attachments, 'rb').read())
            att['Content-Type'] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="{}"'.format(att_name)
            msg.attach(att)

        smtp = smtplib.SMTP_SSL(self.host, self.port)
        # smtp.set_debuglevel(2)
        try:
            smtp.ehlo()
            smtp.login(self.user, self.password)
            smtp.sendmail(self.user, to, msg.as_string())
            log.info(" 📧 Email sent successfully!!")
        except BaseException as msg:
            log.error('❌ Email failed to send!!' + msg.__str__())
        # finally:
        # smtp.quit()
