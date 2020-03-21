import smtplib
from email.header import Header
from email.mime.text import MIMEText


class Notifier:
    _from: Header = Header("自动打卡小助手", 'utf-8')
    _to: Header = Header("小主", 'utf-8')

    def __init__(self, host: str, port: int, username: str, password: str, admin_mail: str, mail_ssl: bool):
        if mail_ssl:
            self._svr: smtplib.SMTP_SSL = smtplib.SMTP_SSL(host, port)
        else:
            self._svr: smtplib.SMTP = smtplib.SMTP()
            self._svr.connect(host, port)
        self._svr.login(username, password)
        self._sender = username
        self._admin_mail = admin_mail

    def send(self, receiver: str, subject: str, content: str):
        try:
            message = MIMEText(content, 'plain', 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')
            message['From'] = self._from
            message['To'] = self._to

            self._svr.sendmail(self._sender, receiver, message.as_string())
        except Exception:
            pass

    def alert(self, subject: str, content: str):
        self.send(self._admin_mail, subject, content)
