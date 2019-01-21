import smtplib
from emial.mime.text import MIMETest
from email.header import Header

sender = 'from@runob.com'
receiver = ['1163645478@qq.com','2741500014@qq.com']

message = MIMETest('CESHI','plain','utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'ceshi'
message['Subject'] = Header(subject,'utf-8')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")