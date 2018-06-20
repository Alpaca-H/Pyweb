# -*- coding:utf-8 -*-
__author__ = 'hzj'

#独立使用django的model
import sys
import os

#获取当前文件的路径
pwd = os.path.dirname(os.path.realpath(__file__))

#找到项目文件
sys.path.append(pwd+"../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hzj_rest_test.settings")

import django
django.setup()


from goods.models import Goods,GoodsCategory,GoodsImage

#添加数据开始

from db_tools.data.product_data import row_data


for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail['name']
    goods.market_price =float( int(goods_detail["market_price"].replace("￥","").replace("元","")))
    goods.market_price =float( int(goods_detail["sale_price"].replace("￥","").replace("元","")))
    goods.goods_brief = goods_detail['desc'] if goods_detail['desc'] is not None else ""
    goods.goods_desc = goods_detail['goods_desc'] if goods_detail['goods_desc'] is not None else ""

    category_name = goods_detail['categorys'][-1]
    category = GoodsCategory.objects.filter()
    if category:
        goods.category = category[0]
    goods.save()

    for goods_image in goods_detail['images']:
        goods_image_instance  = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()



