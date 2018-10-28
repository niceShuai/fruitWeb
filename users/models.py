from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='用户名')
    user_pwd = models.CharField(max_length=32, verbose_name='密码')  #md5 code 32bit
    user_email = models.CharField(max_length=30, verbose_name='邮箱')
    receive_name = models.CharField(max_length=20, default='', verbose_name='收货人姓名')
    receive_addr = models.CharField(max_length=30, default='', verbose_name='收货地址')
    receive_phone = models.CharField(max_length=11, default='', verbose_name='收货人手机号')
    receive_postcode = models.CharField(max_length=6, default='', verbose_name='邮编')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


