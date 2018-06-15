from  django.urls import path,include,re_path
from . import views



urlpatterns = [

   # path('',views.Index_View.as_view()),
    path('index/',views.Index_View.as_view(),name = 'index'),
    path('Blog/',views.Blog_view_None.as_view(),name = 'Blog'),
    path('Blog/<int:pk>/',views.Blog_view.as_view(),name = 'Blog'),
    path('sw/',views.sw_view.as_view(),name = 'sw'),
    path('art/',views.testView.as_view() ,name= 'art'),
    path('about/',views.aboutView.as_view() ,name= 'about'),
    path('',views.Index_View.as_view(),name = 'index_view'),
    path('login/',views.login_load),
    path('logout/',views.logout_load,name="dsds"),
   # re_path('[\s\S]*?/comment',views.comment,name='me'),
]