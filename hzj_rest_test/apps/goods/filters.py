# -*- coding:utf-8 -*-
__author__ = 'hzj'

import django_filters
from .models import Goods


class ProductFilter(django_filters.rest_framework.FilterSet):
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
    price_min = django_filters.NumberFilter(name="shop_price",lookup_expr="gte")
    price_max  = django_filters.NumberFilter(name="shop_price",lookup_expr="lte")
    test_char  = django_filters.CharFilter(name="name")
    class Meta:
        model = Goods
        fields = ['price_min','price_max','test_char']