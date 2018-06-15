from django.contrib import admin

# Register your models here.
from .models import Article,Commets,Users,Study_Sort,abou_test
import xadmin



class ArticleAdmin(object):
    list_display = ['time','read_sum','like_sum','theme']
    search_fields = ['theme']
    list_filter = ['theme','time']
xadmin.site.register(Article,ArticleAdmin)




class CommentsAdmin(object):
    list_display = ['time', 'commenter', 'comment_sum', 'text']
    search_fields = ['time']
    list_filter = ['time']
xadmin.site.register(Commets, CommentsAdmin)


class UserAdmin(object):
    pass



class Study_sort_Admin(object):
    list_display = ['image','name','study_tag','study_fire']
    list_filter = ['time']

xadmin.site.register(Study_Sort,Study_sort_Admin)


class abou_testAdmin(object):
    list_display = ['name','link']
    List_filter = ['name']


xadmin.site.register(abou_test,abou_testAdmin)


class UsersAdmin(object):
    pass
xadmin.site.register(Users,UsersAdmin)