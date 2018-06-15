# -*- coding:utf-8 -*-
__author__ = 'hzj'


from django.urls import path,include
from .views import OrgView,Add_UseAsk,Teacher_detail,Teacher_list


app_name = "organization"
urlpatterns = [
    path('org-list/',OrgView.as_view(),name="org_list"),
    path('Add_UseAsk/',Add_UseAsk.as_view(),name = "add_useask"),


    path('teacher_datil/',Teacher_detail.as_view(),name= "detail"),
    path('teacher_list/',Teacher_list.as_view(),name = "list")
]