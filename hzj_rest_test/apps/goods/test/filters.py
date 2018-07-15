# -*- coding:utf-8 -*-
__author__ = 'hzj'

import django_filters
from goods.models import Goods
from django.db.models import Q

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    # filters.LOOKUP_TYPES = [
    #     ('', '---------'),
    #     ('exact', 'Is equal to'),
    #     ('not_exact', 'Is not equal to'),
    #     ('lt', 'Lesser than'),
    #     ('gt', 'Greater than'),
    #     ('gte', 'Greater than or equal to'),
    #     ('lte', 'Lesser than or equal to'),
    #     ('startswith', 'Starts with'),
    #     ('endswith', 'Ends with'),
    #     ('contains', 'Contains'),
    #     ('not_contains', 'Does not contain'),
    # ]
    pricemin = django_filters.NumberFilter(name="shop_price",lookup_expr="gte")
    pricemax  = django_filters.NumberFilter(name="shop_price",lookup_expr="lte")
    top_category = django_filters.NumberFilter(method='top_category_filter')


    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))


    class Meta:
        model = Goods
        fields = ['pricemax','pricemin']