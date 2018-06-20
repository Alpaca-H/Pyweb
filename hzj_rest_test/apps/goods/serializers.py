# -*- coding:utf-8 -*-
__author__ = 'hzj'

from rest_framework import serializers
from .models import GoodsCategory,Goods

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length= 100)
#     # click_num = serializers.IntegerField(required=True)
#
#     def create(self, validated_data):#创建
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)
#
#     #创建字段，这里会收集字典，balidated_data并将内容进行objects.create
#
#
#     # def update(self, instance, validated_data): #修改
#     #     """
#     #     Update and return an existing `Snippet` instance, given the validated data.
#     #     """
#     #     instance.title = validated_data.get('title', instance.title)
#     #     instance.code = validated_data.get('code', instance.code)
#     #     instance.linenos = validated_data.get('linenos', instance.linenos)
#     #     instance.language = validated_data.get('language', instance.language)
#     #     instance.style = validated_data.get('style', instance.style)
#     #     instance.save()
#     #     return instance


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"




class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()  #利用主键字段实例化，进行嵌套
    class Meta:
        model  = Goods
        # fields = ["name","click_num","market_price","add_time"]
        fields = "__all__"
