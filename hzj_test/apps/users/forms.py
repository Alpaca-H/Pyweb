# -*- coding:utf-8 -*-
from captcha.fields import CaptchaField

__author__ = 'hzj'

from django import forms

class loginForm(forms.Form):
    username = forms.CharField(required=True)#加上这个以后，如果字段为空，就会报错
    password = forms.CharField(required=True,min_length=5)


#form下的username password必须和前台的name相等


class CaptchaTestModelForm(forms.Form):
    #校验验证码和邮箱
    captcha = CaptchaField()
    email = forms.EmailField(required=True,min_length=5)



class forgetCaptcha(forms.Form):
    captcha = CaptchaField()
    email = forms.EmailField(required=True, min_length=5)
