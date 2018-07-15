# -*- coding:utf-8 -*-
__author__ = 'hzj'


from django.urls import path,include
from .views import OrgView,Add_UseAsk,\
    Teacher_detail,Teacher_list,org_detail_homepage,\
    org_detail_course,org_detail_desc,org_detail_teachers


app_name = "organization"
urlpatterns = [
    path('org-list',OrgView.as_view(),name="org_list"),
    path('Add_UseAsk/',Add_UseAsk.as_view(),name = "add_useask"),
    path('teacher_datil/',Teacher_detail.as_view(),name= "detail"),
    path('teacher_list/',Teacher_list.as_view(),name = "list"),
    path('org-detail-homepage/<int:org_id>',org_detail_homepage.as_view(),name='detail_homepage'),
    # path('org-detail-homepage/', org_detail_homepage.as_view(), name='detail_homepage'),
    path('org-detail-course/<int:org_id>', org_detail_course.as_view(), name='detail_course'),
    path('org-detail-desc/<int:org_id>', org_detail_desc.as_view(), name='detail_desc'),
    path('org-detail-teachers/<int:org_id>', org_detail_teachers.as_view(), name='detail_teachers')

]