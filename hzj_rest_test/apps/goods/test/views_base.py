# -*- coding:utf-8 -*-
__author__ = 'hzj'
from django.views.generic.base import View
from django.views.generic import ListView,DetailView,TemplateView
from goods.models import Goods
import json
from django.http import HttpResponse,JsonResponse
from django.core import serializers  # 序列化
class GoodListView(View):
    """
    使用json返回商品列表页信息

    """
    def get(self,request):
        goods_list = Goods.objects.all()[:10]
        json_list = []
        # for goods in goods_list:
        #     json_dict = {}
        #     json_dict['name'] = goods.name
        #     json_dict['category'] = goods.category.name
        #     json_dict['market_price'] = goods.market_price
        #     json_list.append(json_dict)
        json_data = serializers.serialize("json",goods_list)
        json_data = json.loads(json_data)#转成字典
        #return HttpResponse(json.dumps(json_data), content_type='application/json')
        return JsonResponse(json_data,safe=False)

    # #写法2
    # def get(self,request):
    #     goods_list = Goods.objects.all()[:10]
    #     json_list = []
    #     from django.forms.models import model_to_dict  # 字段变成字典
    #
    #     for goods in goods_list:
    #         json_dict = model_to_dict(goods)
    #         json_list.append(json_dict)
    #         # json_dumps转换需要符合json格式
    #     return HttpResponse(json.dumps(json_list), content_type='application/json')








