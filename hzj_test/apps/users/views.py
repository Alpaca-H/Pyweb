from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from  django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from users.utils.email_send import send_register_email

from django.views.generic import View
from users.forms import loginForm,CaptchaTestModelForm,forgetCaptcha

from  .models import EmailVerifyRecord

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            #传再django里面的时密文，传出来的时铭文，输入的也时明文，无法匹配，所以我们这里只查username
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))    #username表示之前我们输入的username他可以表示我们输入的账号
            #其中包括电话，邮箱还有账号
            #Q语法的使用 Q()|Q()  表示或  Q(),Q() 表示并且
            #check_password将密码加密进行比较
            if user.check_password(password):
                return user
        except Exception as e:
            return None






def logout_te(request):
    logout(request)
    return render(request,'index.html')





#基于类

#这里的get直接可以获取username和password,基于类的话他可以自定定义时post请求还是get请求
class Login_View(View):
    def post(self,request):
        form = loginForm(request.POST)  #传进来一个字典的参数
        if form.is_valid():    #判断是否符合form表单要求
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request,'login.html',{'message':'账号未激活'})
            else:
                return render(request,'login.html',{'message':'账号密码错误'})
        else:
            return render(request, 'login.html', {'form_message':form})
    def get(self,request):
        return  render(request,'login.html')




class registerview(View):
    def get(self,request):
        registers = CaptchaTestModelForm()
        return render(request,'register.html',{'registers':registers})
    def post(self,request):
        form = CaptchaTestModelForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'form_message':form,'message': "用户已经存在"})
            password = request.POST['password']
            user = UserProfile()
            #django后台的密码为has加密密码，我们要在这里对他进行加密
            user.password = make_password(password)
            user.email = email
            user.username = email
            user.is_active = False  #表明未激活，需要从邮箱中去激活
            user.save()
            send_register_email(email,'register')
            return render(request,'index.html')
        else:
            return render(request,'register.html',{'form_message':form})



class activeView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                record_email = record.email
                user = UserProfile.objects.get(email=record_email)
                user.is_active = True
                user.save()
            return HttpResponse("注册成功"
                                "<a>前往登陆</a>")
        else:
            return HttpResponse("注册失败"
                                "<a>前往登陆</a>")



class ForgetPassword(View):
    def get(self,request):
        form = forgetCaptcha()
        return render(request,'forgetpwd.html',{'form_message':form})

    def post(self,request):
        form = forgetCaptcha(request.POST)
        if form.is_valid():
            email = request.POST['email']

            send_register_email(email, 'forget')
        return render(request,'login.html',{})

class updatePassword(View):
    def get(self,request,password):
        all_records = EmailVerifyRecord.objects.filter(code=password)
        if all_records:
            for record in all_records:
                mail = record.email
                user = UserProfile.objects.get(email=mail)
                password = "123456789"
                new_password = make_password(password)
                user.password = new_password
                user.save()
                return  render(request,'login.html')
        else:
            return  render(request,'login.html')





#不基于类
# def login_te(request):
#     if request.method =="POST":
#         user_name = request.POST.get("username","")
#         pass_word = request.POST.get("password","")
#         user = authenticate(username=user_name,password=pass_word)
#         if user is not None:
#             login(request,user)
#             return render(request,'index.html')
#         else:
#             return render(request,'login.html',{'message':"账号密码错误"})
#     elif request.method=="GET":
#         return  render(request,'login.html',{})


