# -*- coding:utf-8 -*-
__author__ = 'hzj'


from django.urls import path,include
from .import views

urlpatterns=[

    path('test/',views.test),
    path('index/',views.index)

]