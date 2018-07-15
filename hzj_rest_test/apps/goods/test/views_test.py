# Create your views here.
#rest API写法

from goods.models import Goods
from goods.test.serializers import GoodsSerializer  #引用外部写好的serialize.py文件

#更牛逼
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination



#超级牛逼
from rest_framework import  viewsets


#超级牛逼
class GoodListViewset(viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer



#过滤
from django_filters.rest_framework import DjangoFilterBackend
from goods.test.filters import GoodsFilter


#rest_framework  过滤

#牛逼
#重写分页
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 1000


class GoodListView(generics.ListAPIView):
    """
    商品列表页
    """


    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    pagination_class = LargeResultsSetPagination
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    filter_backends = (DjangoFilterBackend)  # 过滤
    filter_fields = ('name','shop_price') #过滤
    filter_class = GoodsFilter  # 自定义过滤


    search_fields = ('shop_price', 'name')




# class GoodListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     这些是一些注释，会在rest页面的options里面显示
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#
#
#     #收集前端内容报错，post
#     def post(self, request, format=None):
#         #会将全部的内容保存在data里面
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
