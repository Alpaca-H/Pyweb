import markdown
from django.shortcuts import render
from .models import Blog, Comment,Per_Read
from django.http import  HttpResponseRedirect,HttpResponse
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 内置


def load(requests):
    return render(requests, 'load/load.html')


# def index(requests):
#    post = Blog.objects.all()
#    return render(requests,'load/index.html',context={'post_list':post})


def about(requests):
    pr = Per_Read.objects.get(pk=1)
    return render(requests,'load/about.html',{'pr':pr})


# 简答的跳转联系页面
def contact(requests):
    return render(requests, 'load/contact.html')


# 页面跳转附加在继续阅读的a标签上面
def readGo(requests, ueser_id):
    post = Blog.objects.get(pk=ueser_id)
    post.text = markdown.markdown(post.text, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc', ])
    post.views_insert()
    return render(requests, 'load/Blog.html', context={'post': post})


# 在博客主页进行继续阅读跳转  附加在a标签里面
def full(requests, idd):
    post = Blog.objects.get(pk=idd)
    return render(requests, 'load/full-width.html', context={'post': post})


# 简单的跳转博客主页
def fulll(requests):
    post = Blog.objects.all()
    return render(requests, 'load/full-width.html', context={'post': post})


# 跳转到博客页面首页的时候进行简单的分页
def index(requests):
    post = Blog.objects.all()
    pp = post
    p = Paginator(post, per_page=3)  # 输入列表内容，每几个分为一页
    page = requests.GET.get('page')
    update_post_list = post[:3]
    try:
        post = p.page(page)
    except PageNotAnInteger:  # 如果用户请求的页码不是整数，显示第一页
        post = p.page(1)
    except EmptyPage:  # 如果用户请求的页码超过最大页码，显示最后一页
        post = p.page(p.num_pages)
    return render(requests, 'load/index.html',
                  context={'post_list': post, 'update_post_list': update_post_list, 'pp': pp})


def zongjie(requests):
    return render(requests,'load/zongjie.html')


def single(requests):
    return  render(requests,'load/single.html')

def spdier(requests):
    return  render(requests,'load/spider.html',{"ddd":"我的爬虫"})


from django.core.mail import send_mail

def mail(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    email_all_text = '''
        --------------------这是用户 :  %s   发送给你的邮箱---------------------
        name:%s
        subject:%s
        ---------------------------message-----------------------------------
        %s
                                        
                                        
                                    ....请做好查收
    '''%(email,name,subject,message)
    send_status = send_mail(message=email_all_text,from_email="1097690268@qq.com",fail_silently=False,subject="dsds",recipient_list=["1097690268@qq.com","1097690268@qq.com"])

    if send_status:
        print(send_status)
    else:
        print(send_status)
    return render(request,'load/contact.html')


