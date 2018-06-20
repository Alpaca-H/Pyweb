from django.db import models
from datetime import datetime

# Create your models here.

#引用user表的做法
#from users.models import UserProfile   #但在使用这种方式引用的时候，我们在做第三方登录的时候就会出现错误
#或者
from django.contrib.auth import get_user_model
User = get_user_model()
# try:
#     return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
# except ValueError:
#     raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
# except LookupError:
#     raise ImproperlyConfigured(
#         "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
#     )


from goods.models import Goods


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,verbose_name="商品",on_delete=models.CASCADE)
    nums = models.IntegerField(default=0,verbose_name="购买数量")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name,self.nums)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS=(
        ('success',"成功"),
        ('cancel',"取消"),
        ('wait',"待支付"),
    )
    # PAY_TYPE = (
    #     ("alipay","支付宝"),
    #     ("wechat","微信"),
    # )
    user = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=30,verbose_name="订单号")
    trade_no = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name="支付宝订单号")
    pay_status = models.CharField(choices=ORDER_STATUS,max_length=10,verbose_name="订单状态")
    post_script = models.CharField(max_length=11,verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0,verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True,blank=True,verbose_name="支付时间")


    #购买时,填写的用户信息
    address = models.CharField(max_length=100,default="",verbose_name="收获地址")
    signer_name = models.CharField(max_length=20,default="",verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11,verbose_name="联系电话")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.order_sn


class OrderGoods(models.Model):
    """
    订单商品详情
    """
    order = models.ForeignKey(OrderInfo,verbose_name="订单详情",on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,verbose_name="商品",on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0,verbose_name="商品数量")

    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name  = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn