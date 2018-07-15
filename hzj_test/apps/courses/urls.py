# -*- coding:utf-8 -*-
__author__ = 'hzj'


from django.urls import path,include
from courses.views import courselistView,coursecommentView,coursedetailView,coursevideoView

app_name = 'courses'
urlpatterns = [
    path('list/',courselistView.as_view(),name="courses-list"),
    path('course-detai/<int:course_id>', coursedetailView.as_view(), name='course_detail'),
    path('course-comment/<int:course_id>', coursecommentView.as_view(), name='course_comment'),
    path('course-video/<int:course_id>', coursevideoView.as_view(), name='course_video')
]