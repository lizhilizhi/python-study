import  smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender = '2741500014@qq.com'
my_pass = 'imnyzqmffohwdeag'
my_user = '3313505900@qq.com'

def mail():
    ret =True
    try:
        msg = MIMEText('填写邮件问题','plain','utf-8')
        msg['From']=formataddr(["发件人名称",my_sender])
        msg['To'] = formataddr(["收件人测试",my_user])
        msg['Subject'] = "邮件主题-测试"

        server =smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(my_sender,my_pass)
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception:
        ret =False
    return ret


ret = mail()
if ret:
    print("chenggong")
else:
    print("shibai")


