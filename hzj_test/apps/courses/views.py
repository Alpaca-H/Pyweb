# -*- coding:utf-8 -*-
__author__ = 'hzj'

from django.shortcuts import render

# Create your views here.

from django.views.generic import  View
from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
class courselistView(View):
    def get(self,request):
        all_course  = Course.objects.all()
        hot_courses = all_course[:3]

        keywords = request.GET.get('keywords')
        if keywords:
            all_course=all_course.filter(Q(name__icontains=keywords)|Q(students__icontains=keywords))
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 12, request=request)
        courses = p.page(page)

        return render(request,'course-list.html',{
            'courses':courses,
            'hot_courses':hot_courses,
                                                  })


class coursecommentView(View):
    def get(self,request,course_id):
        return  render(request,'course-comment.html',{'course_id':course_id})

class coursedetailView(View):
    def get(self,request,course_id):
        course_detail = Course.objects.get(id=int(course_id))
        lesson_set =course_detail.lesson_set.count()
        usercourse_set = course_detail.usercourse_set.all()[:3]

        return  render(request,'course-detail.html',{
            'course_detail':course_detail,
            'lesson_set':lesson_set,
            'usercourse_set':usercourse_set,
            'course_id':course_id
        })


class coursevideoView(View):
    def get(self,request,course_id):
        return  render(request,'course-video.html',{'course_id':course_id})