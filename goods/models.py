from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class GoodsType(models.Model):
    """商品分类"""
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '商品分类'

class GoodsInfo(models.Model):
    """商品详细信息"""
    name = models.CharField(max_length=30, verbose_name='商品名称')
    pic = models.ImageField(upload_to='goods', verbose_name='商品预览图')
    price = models.DecimalField(max_digits=8 ,decimal_places=2, verbose_name='商品价格')
    unit = models.CharField(max_length=10, verbose_name='计量单位')
    intro = models.CharField(max_length=100, verbose_name='商品简介')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除')
    profile = HTMLField(verbose_name='商品详细介绍')
    click = models.IntegerField(verbose_name='点击量')
    type = models.ForeignKey('GoodsInfo', verbose_name='所属类别')

    class Meta:
        verbose_name = '商品详细信息'


