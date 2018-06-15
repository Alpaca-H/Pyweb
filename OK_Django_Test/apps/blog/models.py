from django.db import models
import  time
from  django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    time = models.DateTimeField(default=timezone.now,verbose_name='时间')
    read_sum = models.IntegerField(default=0,verbose_name='阅读数量',blank=True,null=True)
    like_sum = models.IntegerField(default=0,verbose_name='点赞数',blank=True)
    title = models.CharField(max_length=20,default=None,verbose_name='标题')
    name = models.CharField(max_length=20,default=None,verbose_name='文章题目')
    theme = models.CharField(max_length=10,verbose_name='主题')
    author = models.CharField(max_length=5,default="何泽君",verbose_name='作者')
    write_sum = models.IntegerField(verbose_name='字数')
    text = models.TextField(verbose_name="内容",default=None)
    update_text = models.CharField(max_length=50,verbose_name='更新内容',blank=True,null=True)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering =['-time']


class Commets(models.Model):
    comment_sum = models.IntegerField(default=0,verbose_name='评论量')
    time = models.DateTimeField(default=timezone.now,verbose_name='评论时间')
    commenter = models.CharField(max_length=20,verbose_name='评论人员')
    text = models.TextField(verbose_name="内容",default=None)
    name = models.CharField(max_length=20,default=0,verbose_name='别名')
    mail = models.EmailField(max_length=20,verbose_name='邮箱',default=0)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-time']


    def __str__(self):
        return self.commenter

class Users(User):
    Can_reader = models.CharField(max_length=3,verbose_name="是否可以使用权限")


class Study_Sort(models.Model):
    name = models.CharField(max_length=20,verbose_name='分类名称')
    image = models.ImageField(upload_to='img',default='/img/5.jpg',verbose_name="上传图片")
    study_tag = models.CharField(max_length=10,verbose_name='标签',default=None)
    study_tag_two = models.CharField(max_length=10,verbose_name='标签1',default=None)
    study_tag_three = models.CharField(max_length=10,verbose_name='标签2',default=None)
    study_fire = models.IntegerField(default=0,verbose_name='学习热度')
    time = models.DateTimeField(default=timezone.now,verbose_name="制定时间")
    YEAR_IN_SCHOOL_CHOICES = (
        ('web开发', 'web开发'),
        ('网络安全', '网络安全'),
        ('爬虫', '爬虫'),
        ('自然语言处理', '自然语言处理'),
    )
    study_tag_select = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES,max_length=20,default=0,verbose_name='标签')
    class Meta():
        verbose_name = "学习分类"
        verbose_name_plural = verbose_name
        ordering = ['-time']


    def __str__(self):
        return self.name




class abou_test(models.Model):
    name = models.CharField(max_length=20,default='')
    link = models.CharField(max_length=100,default='#')
    time = models.DateTimeField(default = timezone.now)


    class Meta():
        verbose_name = '关于'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name
#artical
#update





