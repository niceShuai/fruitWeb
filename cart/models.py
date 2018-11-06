from django.db import models


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('users.UserInfo', verbose_name='用户')
    goods = models.ForeignKey('goods.GoodsInfo', verbose_name='商品')
    count = models.IntegerField(default=0, verbose_name='数量')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
