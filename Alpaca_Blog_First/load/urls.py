from django.urls import path,include
from  . import views



urlpatterns = [
    path('',views.index),
    path('index/',views.index,name="app_index"),
    path('load/',views.load),
    path('about/',views.about,name="app_about"),
    path('contact/',views.contact, name="app_contact"),
    path('full/<int:idd>/', views.full, name="app_full"),
    path('readGo/<int:ueser_id>/', views.readGo, name="app_readGo"),
    path('full/', views.fulll, name="app_full"),
    path('zongjie/',views.zongjie),
    path('single/', views.single),
    path('spdier/', views.spdier),
    path('mail/', views.mail),
]
