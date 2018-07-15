from django.shortcuts import render

# Create your views here.


from django.views.generic import View

class user_fav_course(View):
    def get(self,request):
        return render(request,'usercenter-fav-course.html')
    def post(self,request):
        return render(request,'usercenter-fav-course.html')

class user_fav_org(View):
    def get(self,request):
        return render(request,'usercenter-fav-org.html')
    def post(self,request):
        return render(request,'usercenter-fav-org.html')

class user_fav_teacher(View):
    def get(self,request):
        return render(request,'usercenter-fav-teacher.html')
    def post(self,request):
        return render(request,'usercenter-fav-teacher.html')

class user_info(View):
    def get(self,request):
        return render(request,'usercenter-info.html')
    def post(self,request):
        return render(request,'usercenter-info.html')

class user_message(View):
    def get(self,request):
        return render(request,'usercenter-message.html')
    def post(self,request):
        return render(request,'usercenter-message.html')

class user_mycourse(View):
    def get(self,request):
        return render(request,'usercenter-mycourse.html')
    def post(self,request):
        return render(request,'usercenter-mycourse.html')