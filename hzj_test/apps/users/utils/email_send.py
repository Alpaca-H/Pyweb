# -*- coding:utf-8 -*-
__author__ = 'hzj'

from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
import hzj_test.settings as settings
from datetime import datetime
#邮箱验证码
def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.send_type =send_type
    email_record.send_time = datetime.now()
    email_record.email = email
    email_record.save()

    email_title =""
    email_body = ""

    if send_type == 'register':
        email_title = "注册链接"
        email_body = "请点击下面的链接进行注册:http://127.0.0.1:8000/active/{0}".format(code)

    if send_type == 'forget':
        email_title = "忘记密码链接"
        email_body = "请点击下面的链接进行账号密码的修改:http://127.0.0.1:8000/get_password/{0}".format(code)
    send_status =  send_mail(email_title,email_body,settings.EMAIL_FROM,[email])
    if send_status:
        print(send_status)
        pass



def random_str(randomlength):
    str=''
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'  #随机字符串
    random = Random()
    for i in range(randomlength):
        str +=chars[random.randint(0,len(chars))]
    return str

