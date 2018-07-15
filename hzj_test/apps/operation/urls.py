# -*- coding:utf-8 -*-
__author__ = 'hzj'

from django.urls import include,path
from operation.views import user_fav_course,user_fav_org,user_fav_teacher,user_info,user_message,user_mycourse
app_name = 'operation'

urlpatterns=[

    path('user_fav_course/',user_fav_course.as_view(),name='user_fav_course'),
    path('user_fav_org/', user_fav_org.as_view(), name='user_fav_org'),
    path('user_fav_teacher/',user_fav_teacher.as_view(),name='user_fav_teacher'),
    path('',user_info.as_view(),name='user_info'),
    path('user_message/',user_message.as_view(),name='user_message'),
    path('user_mycourse/',user_mycourse.as_view(),name='user_mycourse'),

]

