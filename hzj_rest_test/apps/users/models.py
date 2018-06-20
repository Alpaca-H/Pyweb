from datetime import datetime
from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """
    用户
    姓名，出生年月，性别，电话，邮箱
    """
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    birthday =  models.DateField(null=True,blank=True,verbose_name="出生年月")
    gender = models.CharField(max_length=6,choices=(("male","男"),("female","女")),default="male",verbose_name="性别")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name="邮箱")



    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    #上面使用return self.name 会在使用drf的时候报错


class VerifyCode(models.Model):
    """
    短信验证码
    验证码，发送的手机号，添加时间，
    """
    code = models.CharField(max_length=10,verbose_name="验证码")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    add_time = models.DateTimeField(max_length=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code