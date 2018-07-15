# -*- coding:utf-8 -*-


__author__ = 'hzj'

from rest_framework import mixins,viewsets
from goods.models import Goods,GoodsCategory
from goods.test.serializers import GoodsSerializer,CategorySerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from goods.test.filters import GoodsFilter

class Goods_ResultsSetPagination(PageNumberPagination):
    page_size = 10        #指示页面大小的数值
    page_size_query_param = 'page_size'  #指示查询参数的名称，允许客户端根据每个请求设置页面大小。默认为None，表示客户端可能无法控制所请求的页面大小。
    page_query_param = 'page'  #设置头部
    max_page_size = 10 #表示允许的最大页面大小。该属性仅在page_size_query_param设置时才有效。

class Goods_List_ViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()  #收集参数
    serializer_class =  GoodsSerializer #指定序列化类
    pagination_class = Goods_ResultsSetPagination  #指定分页类
    #django自带的过滤器django_filters.rest_framework import djangofilterbackend
    #rest_framework 自带的过滤器，搜索和排序

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

    filter_class =GoodsFilter  #自定义过滤类

    search_fields = ("=name","goods_brief","goods_desc") #搜索字段
    ordering_fields = ('sold_num','add_time')



class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset =GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
