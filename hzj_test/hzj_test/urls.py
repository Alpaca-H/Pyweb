"""hzj_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
import xadmin
from django.views.generic import TemplateView
from users.views import Login_View,logout_te,registerview,activeView,ForgetPassword,updatePassword
from organization.views import OrgView
from django.views.static import serve
from hzj_test.settings import MEDIA_ROOT
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name = "index"),
    path('login/',Login_View.as_view(),name = 'login'),
    path('logout/',logout_te,name = 'logout'),
    path('register/',registerview.as_view(),name='register'),
    re_path('active/(?P<active_code>.*)/$',activeView.as_view(),name="activeView"),
    path('forget_password/',ForgetPassword.as_view(),name="forget_password"),
    re_path('get_password/(?P<password>.*)/$',updatePassword.as_view(),name='updatePassword'),
    re_path(r'^captcha/', include('captcha.urls')),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),


    path('org/',include('organization.urls',namespace="org"))



]
