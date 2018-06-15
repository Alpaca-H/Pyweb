
from django.shortcuts import render
from django.http import HttpResponse
import logging
import json
# Create your views here.
from django.views.generic import ListView,DetailView,TemplateView
from  .models import  Article,Commets,Users,Study_Sort,abou_test
from  django.contrib.auth import authenticate,login,logout
import  markdown
from django.utils import timezone


def login_load(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username,password=password)

        if user is not None:
            login(request,user)
            return_json = {'result':1}
            request.session['name'] = username
            return HttpResponse(return_json['result'])
        else:
            print("登陆错误")
            return_json = {'result': 2}
            return HttpResponse(return_json['result'])

    else:
        return render(request, "blog/index.html")


def logout_load(request):
    logout(request)
    request.session['name'] = None
    return render(request, "blog/index.html")



def comment(request):
    comment_all = Commets.objects.all()
    if request.method == 'POST':
        name = request.POST['name_body']
        mail = request.POST['mail']
        v_name = request.POST['v_name']
        comment = request.POST['comment']
        comment_all.create(name=name,mail=mail,commenter=v_name,text=comment,time=timezone.now,comment_sum=len(comment))
        return  render(request,'/')
    else:
        return render(request,'blog/index.html')


class Index_View(ListView):
    model  = Article
    template_name = 'blog/index.html'
    context_object_name = 'articals'
    extra_context = {'articalss':Article.objects.all()[3:6],'updates':Article.objects.all()[:4]}


    def get_queryset(self):
        articals = Article.objects.all()[:3]
        return articals




class Blog_view(DetailView):
    model = Article
    template_name = 'blog/Blog.html'
    context_object_name = 'artical_list'

    pk_url_kwarg = 'pk'



    def get_object(self, queryset=None):
        artical_list = super(Blog_view,self).get_object(queryset=None)
        artical_list.text = markdown.markdown(artical_list.text,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return artical_list







class Blog_view_None(ListView):
    template_name = 'blog/Blog.html'
    model = Article
    context_object_name = 'artical_list'

    def get_queryset(self):
        artical_list = Article.objects.get(name='欢迎来到我的博客')
        return artical_list


class sw_view(ListView):
    model = Article
    template_name = 'blog/SofeWare_load.html'
    context_object_name = 'artitcals'


class testView(ListView):
    model = Study_Sort
    template_name = 'blog/art_test.html'
    context_object_name = 'object'

    def get_queryset(self):
        object = Study_Sort.objects.all()
        return object



class artView(ListView):
    model = Study_Sort
    template_name = 'blog/art_test.html'
    context_object_name = 'object'

    def get_queryset(self):
        object = Study_Sort.objects.all()[:3]
        return object




class aboutView(ListView):
    model = abou_test
    template_name = 'blog/about.html'
    context_object_name = 'object'
    extra_context = {'object_two':abou_test.objects.all()[6:abou_test.objects.all().count()]}

    def get_queryset(self):
        object = abou_test.objects.all()[:6]
        return  object