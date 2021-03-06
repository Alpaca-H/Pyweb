from django.shortcuts import render

# Create your views here.



from .models import CourseOrg,CityDict
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from organization.forms import UserAskForm
from courses.models import Course



class OrgView(View):

    def get(self,request):
        all_orgs = CourseOrg.objects.all()#所有课程
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        #热门课程等于所有课程根据点击数倒序排序，并取3前三

        all_citys = CityDict.objects.all()
        counts = all_orgs.count()

        city_id = request.GET.get('city','')
        if city_id:
            all_orgs = CourseOrg.objects.filter(city_id=int(city_id))

        sort_cotegory = request.GET.get('ct','')
        if sort_cotegory:
            all_orgs = all_orgs.filter(category=sort_cotegory)



        paixu = request.GET.get('sort','')
        if paixu:
           if paixu =="students":
               all_orgs = all_orgs.order_by('-students')
           elif paixu =="courses" :
                all_orgs = all_orgs.order_by('-course_nums')



        #对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)


        #上面是对页面进行分页，try-except是用来请求得到page参数 如果不合法则返回默认页数为1
        #Paginator对所有的all_orgs进行分类  5条数据为一页，

        return render(request,'org-list.html',{
            'course_orgs': orgs, #分页的
            'all_citys': all_citys,
            'counts':counts,
            'city_id':city_id,
            'sort_cotegory':sort_cotegory,
            'hot_orgs':hot_orgs,
            'paixu':paixu
        })



class Add_UseAsk(View):
    def post(self,request):
        ask_form = UserAskForm(request.POST)
        if ask_form.is_valid():
            ask_form.save(commit=True) #这里可以将form表单直接提交到数据库，如果设定commit=TRUE的话，那么不但会提交到数据库，还会保存再数据库里面
            return HttpResponse("{'status':'success'}",content_type='application/json')
        else:
            return HttpResponse("{'status':'fail','msg':'提交发生错误'}",content_type='application/json')



class Teacher_detail(View):
    def get(self,request):
        return render(request,'teacher-detail.html')

class Teacher_list(View):
    def get(self,request):
        return render(request,'teachers-list.html')

class org_detail_homepage(View):
    def get(self,request,org_id):
        orgs = CourseOrg.objects.get(id=int(org_id))
        all_course = orgs.course_set.all()[:3]
        all_teacher = orgs.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',{'org_id':org_id,'all_course':all_course,'all_teacher':all_teacher})

class org_detail_course(View):
    def get(self,request,org_id):
        return render(request,'org-detail-course.html',{'org_id':org_id})

class org_detail_desc(View):
    def get(self,request,org_id):
        return render(request,'org-detail-desc.html',{'org_id':org_id})

class org_detail_teachers(View):
    def get(self,request,org_id):
        return render(request,'org-detail-teachers.html',{'org_id':org_id})