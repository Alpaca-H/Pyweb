from django.contrib import admin
from .models import Comment,Blog,Per_Read
# Register your models here.

@admin.register(Comment)
class commetAdmin(admin.ModelAdmin):
    list_per_page = 5
    #ordering = ['-time',]



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","times","author","text")
    list_per_page = 10


@admin.register(Per_Read)
class PerAdmin(admin.ModelAdmin):
    pass